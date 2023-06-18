from django.contrib.auth.models import User
from django.views.generic import ListView


class SearchListView(ListView):
    model = User
    template_name = "searchapp/search_list.html"

    def get_queryset(self, *args, **kwargs):
        q = self.request.GET.get("q", "")

        object_list = User.objects.filter(username__icontains=q)

        return object_list
