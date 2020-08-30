from django import forms
from django.forms import ModelForm
from .models import Testimonials


class AddTestimonialsForm(forms.ModelForm):
    """
    return all fields from testimonials models for users to add
    """
    class Meta:
        model = Testimonials
        fields = '__all__'