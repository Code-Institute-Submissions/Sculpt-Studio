from django.db import models
from programs.models import Programs
from user_profile.models import Profile
from django_countries.fields import CountryField
import uuid


class Checkout(models.Model):
    '''
    model for checkout page and purchases
    '''
    order_number = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    program_id = models.OneToOneField(Programs, on_delete=models.CASCADE, null=True)
    billing_address = models.CharField(max_length=256)
    billing_postcode = models.CharField(max_length=15)
    billing_city = models.CharField(max_length=32)
    billing_country = CountryField()
    
    def __str__(self):
        return self.order_number
