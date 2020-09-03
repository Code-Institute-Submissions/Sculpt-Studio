from django.db import models
from phone_field import PhoneField

class Partners(models.Model):
    '''model for handling partners deals'''
    class Meta():
        verbose_name_plural = 'Partners'

    name = models.CharField(max_length=64)
    summary = models.TextField(max_length=1028)
    main_contact = models.CharField(max_length=128)
    main_contact_phone = PhoneField(help_text='Main Contact Phone Number')
    main_contact_email = models.CharField(max_length=64)
    discount = models.DecimalField(max_digits=2, decimal_places=0)
    link = models.URLField(max_length=200)
    deal_validity = models.DateField(null=True, blank=True)
