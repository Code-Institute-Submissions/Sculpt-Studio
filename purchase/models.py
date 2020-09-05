from django.db import models
from programs.models import Programs
from user_profile.models import Profile
from django_countries.fields import CountryField


class Checkout(models.Model):
    '''
    model for checkout page
    '''
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    billing_address = models.CharField(max_length=256)
    billing_postcode = models.CharField(max_length=15)
    billing_city = models.CharField(max_length=32)
    billing_country = CountryField()


