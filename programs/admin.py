from django.contrib import admin
from .models import Programs

# Register your models here.

class ProgramAdmin(admin.ModelAdmin):
    list_display = (
                'name',
                'type',
                'description',
                'price',
    )

admin.site.register(Programs, ProgramAdmin)