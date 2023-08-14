from django import forms

from chatapp.models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["name"]
