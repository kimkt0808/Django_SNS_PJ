from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from chatapp.forms import RoomForm, PasswordForm
from chatapp.models import Room, PrivateRoom


def index(request):
    room_list = Room.objects.all()

    return render(request, "chatapp/index.html", {
        "room_list": room_list,
    })


class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = "chatapp/create_room.html"

    def form_valid(self, form):
        room = form.save(commit=False)
        room.user = self.request.user
        room.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("chatapp:room", kwargs={"room_pk": self.object.pk})


class RoomDetailView(DetailView):
    model = Room
    context_object_name = "room"
    template_name = "chatapp/room.html"

    def get_object(self, queryset=None):
        room_obj = get_object_or_404(Room, pk=self.kwargs["room_pk"])

        return room_obj

    def post(self, request, *args, **kwargs):
        room_obj = self.get_object()
        password_form = PasswordForm(request.POST)

        if password_form.is_valid():
            password = password_form.cleaned_data['password']

            if not password or not room_obj.check_room_password(password):
                messages.error(request, '비밀번호가 일치하지 않거나 제대로 입력하지 않았습니다. 다시 입력해 주세요.')

                origin = request.POST.get('origin', 'index')
                if origin == 'index':
                    return redirect('chatapp:index')
                elif origin == 'room_search_list':
                    base_url = reverse('searchapp:room_search_list')

                    query_string = urlencode({'room_q': room_obj.name})
                    url = f'{base_url}?{query_string}'

                    return redirect(url)

        return super().get(request, *args, **kwargs)


class RoomDeleteView(DeleteView):
    model = Room
    context_object_name = "room"
    success_url = reverse_lazy("chatapp:index")
    template_name = "chatapp/delete_room.html"

    def get_object(self, queryset=None):
        room_obj = get_object_or_404(Room, pk=self.kwargs["room_pk"])

        return room_obj


class RoomUserListView(ListView):
    model = Room

    def get(self, request, *args, **kwargs):
        room = get_object_or_404(Room, pk=self.kwargs["room_pk"])
        user_list = room.get_online_usernames()

        return JsonResponse({
            "username_list": user_list,
        })


class PrivateRoomCreateView(View):
    def get(self, request, *args, **kwargs):
        user2 = User.objects.get(username=self.kwargs["username"])

        room = PrivateRoom.objects.filter(Q(user1=request.user, user2=user2) | Q(user1=user2, user2=request.user)).first()

        if not room:
            room = PrivateRoom(user1=request.user, user2=user2)
            room.save()

        return redirect(reverse("chatapp:private_room", kwargs={"pk": room.pk}))


class PrivateRoomDetailView(DetailView):
    model = PrivateRoom
    context_object_name = "rooms"
    template_name = "chatapp/private_room.html"

    def get(self, request, *args, **kwargs):
        room = self.get_object()

        if request.user != room.user1 and request.user != room.user2:
            return redirect('chatapp:index')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.get_object()

        if room.user1 == self.request.user:
            other_user = room.user2
        else:
            other_user = room.user1

        context['other_user'] = other_user
        context['my_rooms'] = PrivateRoom.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))

        return context


class PrivateRoomListView(ListView):
    model = PrivateRoom
    context_object_name = "my_rooms"
    template_name = "chatapp/private_room_list.html"

    def get_queryset(self):
        return PrivateRoom.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))
