from django import forms
from django.forms import ModelForm
from .models import Checkout


class CheckoutForm(forms.ModelForm):
    '''form to user for purchasing of programs'''

    models = Checkout
    fields = '__all__'