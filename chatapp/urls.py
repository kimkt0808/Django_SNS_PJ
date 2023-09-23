from django.contrib.auth.decorators import login_required
from django.urls import path

from chatapp import views
from chatapp.views import RoomCreateView, RoomDeleteView, RoomDetailView, RoomUserListView, PrivateRoomListView, \
    PrivateRoomDetailView, PrivateRoomCreateView, MarkNotificationsReadView

app_name = "chatapp"

urlpatterns = [
    # index
    path("", views.index, name="index"),

    # Room
    # create, detail, delete, list
    path("create/", login_required(RoomCreateView.as_view()), name="create"),
    path("<str:room_pk>/chat/", login_required(RoomDetailView.as_view()), name="room"),
    path("<str:room_pk>/delete/", login_required(RoomDeleteView.as_view()), name="delete"),
    path("<int:room_pk>/user_list/", RoomUserListView.as_view(), name="user_list"),

    # Private Room
    # create, detail, list
    path("private_room/create/<str:username>/", login_required(PrivateRoomCreateView.as_view()), name="private_room_create"),
    path('<int:pk>/private_room/', login_required(PrivateRoomDetailView.as_view()), name="private_room"),
    path("my_private_rooms/", login_required(PrivateRoomListView.as_view()), name="my_private_rooms"),

    # Private Room
    # notifications
    path('notifications/read/', MarkNotificationsReadView.as_view(), name="mark_notifications_read"),
]
