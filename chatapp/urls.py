from django.urls import path

from chatapp import views

app_name = "chatapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]
