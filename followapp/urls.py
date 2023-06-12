from django.contrib.auth.decorators import login_required
from django.urls import path

from followapp.views import FollowView

app_name = "followapp"

urlpatterns = [
    path("accounts/<int:pk>/", login_required(FollowView.as_view()), name="follow"),
]
