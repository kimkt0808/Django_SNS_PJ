from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from chatapp.models import Room


class RoomForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "채팅방 이름을 입력해주세요."}), label="제목")
    password = forms.CharField(required=False, widget=forms.PasswordInput, label="비밀번호")
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "채팅방에 대한 간단한 설명을 입력해주세요."}), label="설명")
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"placeholder": "이미지를 업로드해주세요."}), label="이미지")

    is_password_set = forms.BooleanField(required=False, widget=forms.CheckboxInput(), label="비밀번호 설정")

    class Meta:
        model = Room
        fields = ["image", "name", "is_password_set", "password", "description"]

    def clean(self):
        cleaned_data = super().clean()
        is_password_set = cleaned_data.get('is_password_set')
        password = cleaned_data.get('password')

        if is_password_set and not password:
            self.add_error('password', ValidationError("비밀번호 설정이 선택되었습니다. 비밀번호를 입력해주세요."))


class PasswordForm(ModelForm):
    password = forms.CharField(required=False, label='비밀번호', widget=forms.PasswordInput)

    class Meta:
        model = Room
        fields = ["password"]
