from django.contrib import admin
from .models import Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ( 
                'user',
                'address',
                'country',

    )

admin.site.register(Profile, UserAdmin)
