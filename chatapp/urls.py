from django.contrib.auth.decorators import login_required
from django.urls import path

from chatapp import views
from chatapp.views import RoomCreateView, RoomDeleteView, RoomDetailView, RoomUserListView

app_name = "chatapp"

urlpatterns = [
    # index
    path("", views.index, name="index"),

    # create, detail, delete, list
    path("create/", login_required(RoomCreateView.as_view()), name="create"),
    path("<str:room_pk>/chat/", login_required(RoomDetailView.as_view()), name="room"),
    path("<str:room_pk>/delete/", login_required(RoomDeleteView.as_view()), name="delete"),
    path("<int:room_pk>/user_list/", RoomUserListView.as_view(), name="user_list"),
]
