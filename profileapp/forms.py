from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "nickname", "introduction", "email", "sex"]


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "nickname", "introduction", "email", "sex"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].disabled = True
        self.fields["sex"].disabled = True
