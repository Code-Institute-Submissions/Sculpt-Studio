from django import forms
from django.forms import ModelForm
from .models import Programs


class ProgramForm(forms.ModelForm):
    """
    return all fields from progrmas model
    """
    class Meta:
        model = Programs
        fields = '__all__'
