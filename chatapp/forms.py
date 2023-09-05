from django import forms
from django.forms import ModelForm

from chatapp.models import Room


class RoomForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "채팅방 이름을 입력해주세요."}), label="제목")
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")
    description = forms.CharField(widget=forms.Textarea, label="설명")

    class Meta:
        model = Room
        fields = ["name", "password", "description"]


class PasswordForm(ModelForm):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)

    class Meta:
        model = Room
        fields = ["password"]
