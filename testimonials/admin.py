from django.contrib import admin
from .models import Testimonials


class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ( 
                'user',
                'review',
                'score',
                'date',
    )

admin.site.register(Testimonials, TestimonialsAdmin)
