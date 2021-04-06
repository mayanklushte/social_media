from django import forms
from .models import *


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'Mobile_No', 'bio', 'link',
                  'profile_picture']
        widgets = {
            'password': forms.PasswordInput()
        }
