from django.contrib.auth.models import User
from django.views.generic import ListView


class SearchListView(ListView):
    model = User
    template_name = "searchapp/search_list.html"

    def get_queryset(self, *args, **kwargs):
        q = self.request.GET.get("q", None)

        if q:
            object_list = User.objects.filter(username__icontains=q)
        else:
            object_list = User.objects.none()

        return object_list
