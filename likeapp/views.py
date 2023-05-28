from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import RedirectView

from feedapp.models import Feed
from likeapp.models import Likes


class LikeFeedView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("feedapp:detail", kwargs={"pk": kwargs["pk"]})

    def get(self, request, *args, **kwargs):
        user = self.request.user
        feed = get_object_or_404(Feed, pk=kwargs["pk"])

        if Likes.objects.filter(user=user, feed=feed).exists():
            Likes.objects.filter(user=user, feed=feed).delete()

            feed.like_cnt -= 1
            feed.save()

            return HttpResponseRedirect(reverse("feedapp:detail", kwargs={"pk": kwargs["pk"]}))
        else:
            Likes(user=user, feed=feed).save()

            feed.like_cnt += 1
            feed.save()
        
        return super(LikeFeedView, self).get(self.request, *args, **kwargs)
