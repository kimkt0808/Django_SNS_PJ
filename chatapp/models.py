from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete

from config.convert_json import JSONEncoder, JSONDecoder


class OnlineUserMixin(models.Model):
    online_user_set = models.ManyToManyField(User, through="RoomMember", blank=True, related_name="joined_room_set")

    class Meta:
        abstract = True

    def get_online_users(self):
        return self.online_user_set.all()

    def get_online_usernames(self):
        qs = self.get_online_users().values_list("username", flat=True)
        return list(qs)

    def is_joined_user(self, user):
        return self.get_online_users().filter(pk=user.pk).exists()

    def user_join(self, channel_name, user):
        try:
            room_member = RoomMember.objects.get(room=self, user=user)
        except RoomMember.DoesNotExist:
            room_member = RoomMember(room=self, user=user)

        is_new_join = len(room_member.channels_names) == 0
        room_member.channels_names.add(channel_name)

        if room_member.pk is None:
            room_member.save()
        else:
            room_member.save(update_fields=["channels_names"])

        return is_new_join

    def user_leave(self, channel_name, user):
        try:
            room_member = RoomMember.objects.get(room=self, user=user)
        except RoomMember.DoesNotExist:
            return True

        room_member.channels_names.remove(channel_name)

        if not room_member.channels_names:
            room_member.delete()
            return True
        else:
            room_member.save(update_fields=["channels_names"])
            return False


class Room(OnlineUserMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="room", null=True)

    name = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    description = models.TextField(max_length=200, null=True)
    # category

    class Meta:
        ordering = ["-pk"]

    @property
    def chat_group_name(self):
        return self.make_chat_group_name(room=self)

    @staticmethod
    def make_chat_group_name(room=None, room_pk=None):
        return "chat-%s" % (room_pk or room.pk)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.password = make_password(self.password)
        super(Room, self).save(*args, **kwargs)

    def check_room_password(self, password):
        return check_password(password, self.password)


def room__on_post_delete(instance: Room, **kwargs):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        instance.chat_group_name,
        {
            "type": "chat.room.deleted",
        }
    )


post_delete.connect(
    room__on_post_delete,
    sender=Room,
    dispatch_uid="room__on_post_delete",
)


class RoomMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    channels_names = models.JSONField(
        default=set,
        encoder=JSONEncoder,
        decoder=JSONDecoder,
    )
