from django.urls import re_path

from chatapp import consumers

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_pk>[^/]+)/chat/', consumers.ChatConsumer.as_asgi()),
    re_path(r'^ws/chat/(?P<room_pk>[^/]+)/private_room/', consumers.PrivateRoomChatConsumer.as_asgi()),
]
