from django.urls import path

from likeapp.views import LikeFeedView

app_name = "likeapp"

urlpatterns = [
    path("feeds/<int:pk>/", LikeFeedView.as_view(), name="like"),
]