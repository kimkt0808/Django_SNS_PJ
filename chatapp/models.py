from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete, post_save
from notifications.signals import notify

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
    description = models.TextField(max_length=30, null=True)
    image = models.ImageField(upload_to="room_images/", blank=False)

    is_password_set = models.BooleanField(default=False, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True)

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


class PrivateRoom(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2")

    @property
    def chat_group_name(self):
        return self.make_chat_group_name(room=self)

    @staticmethod
    def make_chat_group_name(room=None, room_pk=None):
        return "chat-%s" % (room_pk or room.pk)

    def last_message(self):
        return self.messages.order_by('-created_at').first()


class PrivateRoomMessage(models.Model):
    room = models.ForeignKey(PrivateRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']


def send_notification(sender, instance=None, created=False, **kwargs):
    if created:
        recipient = instance.room.user1 if instance.sender != instance.room.user1 else instance.room.user2
        notify.send(instance.sender,
                    recipient=recipient,
                    verb="sent you a message.",
                    description=f"Message in {instance.room.chat_group_name}: {instance.content}")


post_save.connect(send_notification, sender=PrivateRoomMessage)
