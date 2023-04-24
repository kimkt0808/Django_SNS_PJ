from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_check
from accountapp.forms import UserEditForm


def index(request):
    return HttpResponse("Hello World!")


class AccountSignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("accountapp:login")
    template_name = "accountapp/signup.html"


@method_decorator(account_check, "get")
class AccountDetailView(DetailView):
    model = User
    context_object_name = "my_user"
    template_name = "accountapp/detail.html"


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
