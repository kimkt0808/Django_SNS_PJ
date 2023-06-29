from django import forms
from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreateForm(ModelForm):
    image = forms.ImageField(label="이미지")
    nickname = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "내용을 입력해주세요."}), label="닉네임")
    introduction = forms.CharField(widget=forms.Textarea(attrs={"class": "editable text-start",
                                                                "style": "height: auto;"}), label="소개")
    email = forms.EmailField(label="이메일")
    sex = forms.ChoiceField(label="성별", choices=Profile.SEX_CHOICES)

    class Meta:
        model = Profile
        fields = ["image", "nickname", "introduction", "email", "sex"]


class ProfileEditForm(ModelForm):
    image = forms.ImageField(label="이미지")
    nickname = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "내용을 입력해주세요."}), label="닉네임")
    introduction = forms.CharField(widget=forms.Textarea(attrs={"class": "editable text-start",
                                                                "style": "height: auto;"}), label="소개")
    email = forms.EmailField(label="이메일")
    sex = forms.ChoiceField(label="성별", choices=Profile.SEX_CHOICES)

    class Meta:
        model = Profile
        fields = ["image", "nickname", "introduction", "email", "sex"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].disabled = True
        self.fields["sex"].disabled = True
