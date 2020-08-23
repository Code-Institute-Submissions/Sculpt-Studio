from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=264, blank=True )
    country = CountryField()
    

