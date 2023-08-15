from django.contrib.auth.decorators import login_required
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
            created_form = form.save()
            return redirect("chatapp:room", created_form.pk)
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
