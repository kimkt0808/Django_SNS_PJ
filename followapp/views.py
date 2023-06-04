from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import RedirectView

from followapp.models import Follow


class FollowView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("accountapp:detail", kwargs={"pk": kwargs["pk"]})

    def get(self, request, *args, **kwargs):
        user = self.request.user
        target_user = get_object_or_404(User, pk=kwargs["pk"])

        follow = Follow.objects.filter(user=user, follow_user=target_user)

        if follow.exists():
            follow.delete()
        else:
            Follow(user=user, follow_user=target_user).save()

        return super(FollowView, self).get(request, *args, **kwargs)
