from django.db import models

class Partners(models.Model):
    '''model for handling partners deals'''
    class Meta():
        verbose_name_plural = 'Partners'

    name = models.CharField(max_length=64)
    summary = models.TextField(max_length=1028)
    main_contact = models.CharField(max_length=128)
    main_contact_phone = models.IntegerField()
    main_contact_email = models.CharField(max_length=64)
    discount = models.DecimalField(decimal_places=2, max_digits=2)
    link = models.URLField(max_length=200)
    deal_validity = models.DateField(null=True, blank=True)
