from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountSignupView, AccountDetailView, AccountEditView, AccountDeleteView, FollowerListView, \
    FollowListView

app_name = "accountapp"

urlpatterns = [
    # follow
    path("<int:pk>/follower_list/", FollowerListView.as_view(), name="follower_list"),
    path("<int:pk>/follow_list/", FollowListView.as_view(), name="follow_list"),

    # signup, detail, edit, delete
    path("signup/", AccountSignupView.as_view(), name="signup"),
    path("detail/<int:pk>/", AccountDetailView.as_view(), name="detail"),
    path("edit/<int:pk>/", AccountEditView.as_view(), name="edit"),
    path("delete/<int:pk>/", AccountDeleteView.as_view(), name="delete"),

    # login, logout
    path("login/", LoginView.as_view(template_name="accountapp/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
