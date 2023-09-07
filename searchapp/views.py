from django.contrib.auth.models import User
from django.views.generic import ListView

from chatapp.models import Room


class UserSearchListView(ListView):
    model = User
    template_name = "searchapp/user_search_list.html"

    def get_queryset(self):
        q = self.request.GET.get("q", None)

        if q:
            object_list = User.objects.filter(username__icontains=q)
        else:
            object_list = User.objects.none()

        return object_list


class RoomSearchListView(ListView):
    model = Room
    template_name = "searchapp/room_search_list.html"

    def get_queryset(self):
        q = self.request.GET.get("room_q")

        if q:
            room_list = Room.objects.filter(name__icontains=q)
        else:
            room_list = Room.objects.none()

        return room_list
