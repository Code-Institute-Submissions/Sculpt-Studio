from django.db import models
from programs.models import Programs
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import uuid


class Checkout(models.Model):
    '''
    model for checkout page and purchases
    '''
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    program = models.OneToOneField(Programs, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=128, null=False)
    billing_address = models.CharField(max_length=256)
    billing_postcode = models.CharField(max_length=15)
    billing_city = models.CharField(max_length=32)
    billing_country = CountryField()
    



    def _generate_order_number(self):
        '''
        generate order_number
        '''
        return uuid.uuid4().hex.upper

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number