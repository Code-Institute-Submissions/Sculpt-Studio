from django import forms
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta():
        model = Profile
        exclude = ('user',)
        fields = '__all__'


class UserManagementForm(forms.ModelForm):
    """
    return all fields from django User model for management
    """
    class Meta:
        model = User
        exclude = ('password','groups', 'user_permissions')
        fields = '__all__'

