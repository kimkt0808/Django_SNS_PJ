from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from chatapp.forms import RoomForm
from chatapp.models import Room


def index(request):
    room_list = Room.objects.all()

    return render(request, "chatapp/index.html", {
        "room_list": room_list,
    })


@login_required
def create(request):
    if request.method == "POST":
        form = RoomForm(request.POST)

        if form.is_valid():
            created_room = form.save(commit=False)
            created_room.user = request.user
            created_room.save()
            return redirect("chatapp:room", created_room.pk)
    else:
        form = RoomForm()

    return render(request, "chatapp/create_room.html", {
        "form": form,
    })


@login_required
def room(request, room_pk):
    room_obj = get_object_or_404(Room, pk=room_pk)

    return render(request, "chatapp/room.html", {
        "room": room_obj,
    })


@login_required
def delete(request, room_pk):
    room_obj = get_object_or_404(Room, pk=room_pk)

    if request.method == "POST":
        room_obj.delete()
        messages.success(request, "채팅방이 삭제되었습니다.")

        return redirect("chatapp:index")

    return render(request, "chatapp/delete_room.html", {
        "room": room_obj,
    })


@login_required
def user_list(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)

    if not room.is_joined_user(request.user):
        return HttpResponse("Unauthorized user", status=401)

    username_list = room.get_online_usernames()

    return JsonResponse({
        "username_list": username_list,
    })
