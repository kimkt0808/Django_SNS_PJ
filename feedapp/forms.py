from django.forms import ModelForm

from feedapp.models import Feed


class FeedCreateForm(ModelForm):
    class Meta:
        model = Feed
        fields = ["image", "title", "content"]
