from django.urls import path

from accountapp import views

app_name = "accountapp"

urlpatterns = [
    path("", views.index),
]