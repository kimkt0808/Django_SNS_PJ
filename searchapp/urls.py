from django.urls import path

from searchapp.views import UserSearchListView, RoomSearchListView

app_name = "searchapp"

urlpatterns = [
    # user_search
    path("", UserSearchListView.as_view(), name="user_search_list"),

    # room_search
    path("room-search/", RoomSearchListView.as_view(), name="room_search_list"),
]