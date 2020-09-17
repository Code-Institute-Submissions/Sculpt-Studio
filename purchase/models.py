from django.db import models
from programs.models import Programs
from user_profile.models import Profile
from django_countries.fields import CountryField
from django.utils import timezone
from django.db.models import Sum
import uuid


class Checkout(models.Model):
    '''
    model for checkout page and purchases
    '''
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name='orders')
    total_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    purchase_date = models.DateTimeField(editable=False, auto_now_add=True)
    email = models.EmailField(max_length=128, null=False)
    billing_address = models.CharField(max_length=256)
    billing_postcode = models.CharField(max_length=15)
    billing_city = models.CharField(max_length=32)
    billing_country = CountryField()
    

    def _generate_order_number(self):
        '''
        generate order_number
        '''
        return uuid.uuid4().hex.upper()

    
    def update_total_cost(self):
        '''
        update total cost
        '''
        self.total_cost = self.lineitems.aggregate(Sum('line_item_cost'))['line_item_cost__sum']
        self.save()


    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number



class CheckoutLineItem(models.Model):
    '''
    create line item for purchae for details 
    of ordered programs, cost etc.
    '''
    purchase = models.ForeignKey(Checkout, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    program = models.ForeignKey(Programs, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_item_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0, editable=False)

    def save(self, *args, **kwargs):
        '''
        set line item cost
        '''
        self.line_item_cost = self.program.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.purchase.order_number


