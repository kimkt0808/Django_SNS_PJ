from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from chatapp.models import Room


class ChatConsumer(JsonWebsocketConsumer):
    # INIT
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = ""
        self.room = None

    # CONNECT
    def connect(self):
        user = self.scope["user"]
        room_pk = self.scope["url_route"]["kwargs"]["room_pk"]

        try:
            self.room = Room.objects.get(pk=room_pk)
        except Room.DoesNotExist:
            self.close()
        else:
            self.group_name = self.room.chat_group_name

            is_new_join = self.room.user_join(self.channel_name, user)
            if is_new_join:
                async_to_sync(self.channel_layer.group_send)(
                    self.group_name,
                    {
                        "type": "chat.user.join",
                        "username": user.username,
                    }
                )
            async_to_sync(self.channel_layer.group_add)(
                self.group_name,
                self.channel_name,
            )

            self.accept()

    # DISCONNECT
    def disconnect(self, code):
        user = self.scope["user"]

        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name,
        )

        if self.room is not None:
            is_last_leave = self.room.user_leave(self.channel_name, user)
            if is_last_leave:
                async_to_sync(self.channel_layer.group_send)(
                    self.group_name,
                    {
                        "type": "chat.user.leave",
                        "username": user.username,
                    }
                )

    # DELETE
    def chat_room_deleted(self, message_dict):
        custom_code = 4000
        self.close(code=custom_code)

    # RECEIVE_JSON
    def receive_json(self, content, **kwargs):
        user = self.scope["user"]
        _type = content["type"]

        if _type == "chat.message":
            message_owner = user.username
            message = content["message"]

            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    "type": "chat.message",
                    "message": message,
                    "message_owner": message_owner,
                }
            )
        else:
            print(f"Invalid message type : ${_type}")

    # USER_JOIN
    def chat_user_join(self, event):
        self.send_json({
            "type": "chat.user.join",
            "username": event["username"],
        })

    # USER_LEAVE
    def chat_user_leave(self, event):
        self.send_json({
            "type": "chat.user.leave",
            "username": event["username"],
        })

    # RETURN JSON
    def chat_message(self, event):
        self.send_json({
            "type": "chat.message",
            "message": event["message"],
            "message_owner": event["message_owner"],
        })
