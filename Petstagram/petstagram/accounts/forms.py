from django import forms

from petstagram.accounts.models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)
