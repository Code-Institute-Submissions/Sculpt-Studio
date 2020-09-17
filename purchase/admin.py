from django.contrib import admin
from .models import Checkout, CheckoutLineItem


class CheckoutLineItemsAdmin(admin.TabularInline):
    model = CheckoutLineItem
    readonly_fields = ('program', 'line_item_cost', 'quantity' )


class CheckoutAdmin(admin.ModelAdmin):
    inlines = (CheckoutLineItemsAdmin,)
    list_display = ( 
                'user',
                'order_number',
                'email',
                'purchase_date',
                'billing_address',
                'billing_postcode',
                'billing_city',
                'billing_country',
    )
    readonly_fields = ('user', 'purchase_date', 'total_cost', )
    
admin.site.register(Checkout, CheckoutAdmin)