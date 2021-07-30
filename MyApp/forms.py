from django import forms
from .models import ProfileModel

#create your form here
class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['fname', 'lname', 'tech', 'email', 'photo' ]
