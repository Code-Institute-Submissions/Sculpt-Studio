from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Partners


def partners(request):
    '''all partners view'''

    partners = Partners.objects.all()

    context = {
        'partners': partners
    }
        
    
    return render(request, 'partners/partners.html', context)