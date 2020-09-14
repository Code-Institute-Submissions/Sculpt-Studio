from django.contrib import admin
from .models import Checkout


class CheckoutAdmin(admin.ModelAdmin):
    list_display = ( 
                'user',
                'order_number',
                'email',
                'total_cost',
                'program',
                'purchase_date',
                'billing_address',
                'billing_postcode',
                'billing_city',
                'billing_country',
    )
admin.site.register(Checkout, CheckoutAdmin)