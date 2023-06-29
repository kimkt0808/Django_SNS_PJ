from django import forms
from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreateForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "editable text-start",
                                                           "style": "height: auto;"}), label="댓글 남기기")

    class Meta:
        model = Comment
        fields = ["content"]


class CommentEditForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "editable text-start",
                                                           "style": "height: auto;"}), label="댓글")

    class Meta:
        model = Comment
        fields = ["content"]
