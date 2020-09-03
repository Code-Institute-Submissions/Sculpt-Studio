from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def partners(request):
    '''all partners view'''

    return render(request, 'partners/partners.html')