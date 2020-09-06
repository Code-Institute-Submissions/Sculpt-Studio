from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CheckoutForm
from user_profile.models import Profile
from programs.models import Programs
from django.contrib.auth.models import User

@login_required
def purchase_checkout(request, program_id):
    '''
    return purchase checkout page 
    '''
    profile = get_object_or_404(Profile, user=request.user)
    program = get_object_or_404(Programs, pk=program_id)
    form = CheckoutForm()


    context = {
        'form': form,
        'profile': profile,
        'program': program
    }
    return render(request, 'purchase/purchase_checkout.html', context)

