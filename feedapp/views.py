from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from commentapp.forms import CommentCreateForm
from feedapp.decorators import account_check
from feedapp.forms import FeedCreateForm
from feedapp.models import Feed
from likeapp.models import Likes


class FeedCreateView(CreateView):
    model = Feed
    form_class = FeedCreateForm
    success_url = reverse_lazy("feedapp:list")
    template_name = "feedapp/create.html"

    def form_valid(self, form):
        feed = form.save(commit=False)
        feed.writer = self.request.user
        feed.save()

        return super().form_valid(form)


class FeedDetailView(DetailView, FormMixin):
    model = Feed
    form_class = CommentCreateForm
    context_object_name = "my_feed"
    template_name = "feedapp/detail.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        feed = self.object

        like_or_not = Likes.objects.filter(user=user, feed=feed)

        return super(FeedDetailView, self).get_context_data(Feed=Feed, Likes=like_or_not, **kwargs)


@method_decorator(account_check, "get")
@method_decorator(account_check, "post")
class FeedEditView(UpdateView):
    model = Feed
    context_object_name = "my_feed"
    form_class = FeedCreateForm
    template_name = "feedapp/update.html"

    def get_success_url(self):
        return reverse("feedapp:detail", kwargs={"pk": self.object.pk})


@method_decorator(account_check, "get")
@method_decorator(account_check, "post")
class FeedDeleteView(DeleteView):
    model = Feed
    context_object_name = "my_feed"
    success_url = reverse_lazy("feedapp:list")
    template_name = "feedapp/delete.html"


class FeedListView(ListView):
    model = Feed
    template_name = "feedapp/list.html"

    def get_context_data(self, **kwargs):
        shuffle = Feed.objects.order_by("?")

        return super(FeedListView, self).get_context_data(object_list=shuffle, **kwargs)


class LikeListView(ListView):
    model = Likes
    context_object_name = "like_list"
    template_name = "feedapp/like_list.html"

    def get_context_data(self, **kwargs):
        my_likes = Likes.objects.filter(feed=self.kwargs["pk"])

        return super(LikeListView, self).get_context_data(object_list=my_likes, **kwargs)
