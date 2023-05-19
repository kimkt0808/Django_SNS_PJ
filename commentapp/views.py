from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView

from commentapp.decorators import account_check
from commentapp.forms import CommentCreateForm, CommentEditForm
from commentapp.models import Comment
from feedapp.models import Feed


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = "commentapp/create.html"

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.feed = Feed.objects.get(pk=self.request.POST["feed_pk"])
        comment.writer = self.request.user
        comment.save()
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("feedapp:detail", kwargs={"pk": self.object.feed.pk})


@method_decorator(account_check, "get")
@method_decorator(account_check, "post")
class CommentEditView(UpdateView):
    model = Comment
    form_class = CommentEditForm
    context_object_name = "my_comment"
    template_name = "commentapp/update.html"

    def get_success_url(self):
        return reverse("feedapp:detail", kwargs={"pk": self.object.feed.pk})


@method_decorator(account_check, "get")
@method_decorator(account_check, "post")
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = "my_comment"
    template_name = "commentapp/delete.html"

    def get_success_url(self):
        return reverse("feedapp:detail", kwargs={"pk": self.object.feed.pk})
