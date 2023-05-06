from django.urls import path

from feedapp.views import FeedCreateView, FeedDetailView, FeedEditView, FeedDeleteView, FeedListView

app_name = "feedapp"

urlpatterns = [
    # list
    path("list/", FeedListView.as_view(), name="list"),

    # create, detail, edit, delete
    path("create/", FeedCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", FeedDetailView.as_view(), name="detail"),
    path("edit/<int:pk>/", FeedEditView.as_view(), name="edit"),
    path("delete/<int:pk>/", FeedDeleteView.as_view(), name="delete"),
]