from django.urls import re_path

from chatapp import consumers

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_pk>[^/]+)/chat/', consumers.ChatConsumer.as_asgi()),
]
