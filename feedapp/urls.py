from django.urls import path

from feedapp.views import FeedCreateView, FeedDetailView, FeedEditView, FeedDeleteView, FeedListView, LikeListView

app_name = "feedapp"

urlpatterns = [
    # list
    path("", FeedListView.as_view(), name="list"),
    path("<int:pk>/like_list/", LikeListView.as_view(), name="like_list"),

    # create, detail, edit, delete
    path("create/", FeedCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", FeedDetailView.as_view(), name="detail"),
    path("edit/<int:pk>/", FeedEditView.as_view(), name="edit"),
    path("delete/<int:pk>/", FeedDeleteView.as_view(), name="delete"),
]