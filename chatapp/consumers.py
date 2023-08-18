from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from chatapp.models import Room


class ChatConsumer(JsonWebsocketConsumer):
    # INIT
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = ""

    # CONNECT
    def connect(self):
        room_pk = self.scope["url_route"]["kwargs"]["room_pk"]
        self.group_name = Room.make_chat_group_name(room_pk=room_pk)

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name,
        )

        self.accept()

    # DISCONNECT
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name,
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

    # RETURN JSON
    def chat_message(self, event):
        self.send_json({
            "type": "chat.message",
            "message": event["message"],
            "message_owner": event["message_owner"],
        })
