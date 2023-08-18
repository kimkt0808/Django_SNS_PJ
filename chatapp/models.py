from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete


class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="room")
    name = models.CharField(max_length=20)
    # password
    # description
    # category

    class Meta:
        ordering = ["-pk"]

    @property
    def chat_group_name(self):
        return self.make_chat_group_name(room=self)

    @staticmethod
    def make_chat_group_name(room=None, room_pk=None):
        return "chat-%s" % (room_pk or room.pk)


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
