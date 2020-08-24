from django import forms
from django.forms import ModelForm
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta():
        model = Profile
        exclude = ('user',)
        fields = '__all__'
