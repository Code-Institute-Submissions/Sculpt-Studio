from django import forms
from .models import Programs


class ProgramForm(forms.Form):
    """
    return all fields from progrmas model
    """
    class Meta:
        model = Programs
        fields = '__all__'
