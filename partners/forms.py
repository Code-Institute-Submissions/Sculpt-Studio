from django import forms
from django.forms import ModelForm
from .models import Partners


class PartnerForm(forms.ModelForm):
    """
    return all fields from partners for
    admin users to add new partners
    """
    class Meta:
        model = Partners
        fields = '__all__'