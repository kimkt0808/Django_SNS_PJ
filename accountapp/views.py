from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_check
from accountapp.forms import UserEditForm
from feedapp.models import Feed
from followapp.models import Follow


class AccountSignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("accountapp:login")
    template_name = "accountapp/signup.html"


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = "my_user"
    template_name = "accountapp/detail.html"

    def get_context_data(self, **kwargs):
        my_feeds = Feed.objects.filter(writer=self.get_object())

        follow_or_not = Follow.objects.filter(user=self.request.user, follow_user=self.object)

        followers_cnt = Follow.objects.filter(follow_user=self.kwargs["pk"]).count
        follow_cnt = Follow.objects.filter(user=self.kwargs["pk"]).count

        return super(AccountDetailView, self).get_context_data(follow=follow_or_not, object_list=my_feeds, followers_cnt=followers_cnt, follow_cnt=follow_cnt, **kwargs)


@method_decorator(account_check, "get")
@method_decorator(account_check, "post")
class AccountEditView(UpdateView):
    model = User
    form_class = UserEditForm
    context_object_name = "my_user"
    success_url = reverse_lazy("accountapp:login")
    template_name = "accountapp/update.html"


@method_decorator(account_check, "get")
@method_decorator(account_check, "post")
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = "my_user"
    success_url = reverse_lazy("accountapp:login")
    template_name = "accountapp/delete.html"


class AccountLogoutView(LogoutView):
    next_page = reverse_lazy("chatapp:index")

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        user = request.user

        if user.is_authenticated:
            chat_rooms = user.joined_room_set.all()

            for room in chat_rooms:
                room.user_leave(channel_name=request.channel_name, user=user)

        return super().dispatch(request, *args, **kwargs)


class FollowerListView(ListView):
    model = Follow
    context_object_name = "follower_list"
    template_name = "accountapp/follower_list.html"

    def get_context_data(self, **kwargs):
        followers = Follow.objects.filter(follow_user=self.kwargs["pk"])

        return super(FollowerListView, self).get_context_data(object_list=followers, **kwargs)


class FollowListView(ListView):
    model = Follow
    context_object_name = "follow_list"
    template_name = "accountapp/follow_list.html"

    def get_context_data(self, **kwargs):
        follow = Follow.objects.filter(user=self.kwargs["pk"])

        return super(FollowListView, self).get_context_data(object_list=follow, **kwargs)
