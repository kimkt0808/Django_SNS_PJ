from django.urls import path

from followapp.views import FollowView

app_name = "followapp"

urlpatterns = [
    path("accounts/<int:pk>/", FollowView.as_view(), name="follow"),
]
