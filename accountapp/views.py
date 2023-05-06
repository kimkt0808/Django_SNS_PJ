from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_check
from accountapp.forms import UserEditForm
from feedapp.models import Feed


def index(request):
    return HttpResponse("Hello World!")


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
        return super(AccountDetailView, self).get_context_data(object_list=my_feeds, **kwargs)


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
