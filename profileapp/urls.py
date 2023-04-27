from django.urls import path

from profileapp.views import ProfileCreateView, ProfileEditView

app_name = "profileapp"

urlpatterns = [
    path("create/", ProfileCreateView.as_view(), name="create"),
    path("edit/<int:pk>/", ProfileEditView.as_view(), name="edit"),
]
