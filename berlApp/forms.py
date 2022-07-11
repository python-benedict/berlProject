from django import forms
from .models import DetailedUser

class DetailedUserForm(forms.ModelForm):
    class Meta:
        model = DetailedUser
        fields = "__all__"