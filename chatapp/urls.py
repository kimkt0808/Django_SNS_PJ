from django.urls import path

from chatapp import views

app_name = "chatapp"

urlpatterns = [
    path("", views.index, name="index"),

    path("create/", views.create, name="create"),
    path("<str:room_pk>/chat/", views.room, name="room"),
    path("<str:room_pk>/delete/", views.delete, name="delete"),
]
