from django.http import HttpResponseForbidden

from feedapp.models import Feed


def account_check(func):
    def decorated(request, *args, **kwargs):
        feed = Feed.objects.get(pk=kwargs["pk"])

        if not feed.writer == request.user:
            return HttpResponseForbidden()

        return func(request, *args, **kwargs)

    return decorated
