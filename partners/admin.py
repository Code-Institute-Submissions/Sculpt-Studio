from django.contrib import admin
from .models import Partners


class PartnersAdmin(admin.ModelAdmin):
    list_display = ( 
        'name',
        'summary',
        'main_contact',
        'main_contact_phone',
        'main_contact_email',
        'discount',
        'link',
        'deal_validity',
    )

admin.site.register(Partners, PartnersAdmin)
