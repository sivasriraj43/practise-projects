from django import forms

from .models import User

class ProfileDetail(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','date_of_birth','email','country','state']
    