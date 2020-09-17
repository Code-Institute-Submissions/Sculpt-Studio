from django.contrib import admin
from .models import Checkout, CheckoutLineItem


class CheckoutLineItemsAdmin(admin.TabularInline):
    model = CheckoutLineItem


class CheckoutAdmin(admin.ModelAdmin):
    inlines = (CheckoutLineItemsAdmin,)
    list_display = ( 
                'user',
                'order_number',
                'email',
                'total_cost',
                'purchase_date',
                'billing_address',
                'billing_postcode',
                'billing_city',
                'billing_country',
    )
    
admin.site.register(Checkout, CheckoutAdmin)