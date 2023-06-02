from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_check
from profileapp.forms import ProfileCreateForm, ProfileEditForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    context_object_name = "my_profile"
    template_name = "profileapp/create.html"

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("accountapp:detail", kwargs={"pk": self.object.user.pk})


@method_decorator(profile_check, "get")
@method_decorator(profile_check, "post")
class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    context_object_name = "my_profile"
    template_name = "profileapp/update.html"

    def get_success_url(self):
        return reverse("accountapp:detail", kwargs={"pk": self.object.user.pk})
