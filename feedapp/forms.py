from django import forms
from django.forms import ModelForm

from feedapp.models import Feed


class FeedForm(ModelForm):
    image = forms.ImageField(label="이미지")
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "내용을 입력해주세요."}), label="제목")
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "editable text-start",
                                                           "style": "height: auto;"}), label="내용")

    class Meta:
        model = Feed
        fields = ["image", "title", "content"]
