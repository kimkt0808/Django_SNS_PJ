from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView, CommentEditView

app_name = "commentapp"

urlpatterns = [
    path("create/", CommentCreateView.as_view(), name="create"),
    path("edit/<int:pk>/", CommentEditView.as_view(), name="edit"),
    path("delete/<int:pk>/", CommentDeleteView.as_view(), name="delete"),
]
