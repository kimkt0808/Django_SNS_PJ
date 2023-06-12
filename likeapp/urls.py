from django.contrib.auth.decorators import login_required
from django.urls import path

from likeapp.views import LikeFeedView

app_name = "likeapp"

urlpatterns = [
    path("feeds/<int:pk>/", login_required(LikeFeedView.as_view()), name="like"),
]