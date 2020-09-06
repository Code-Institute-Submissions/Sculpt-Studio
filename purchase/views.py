from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CheckoutForm
from user_profile.models import Profile
from programs.models import Programs
from django.contrib.auth.models import User
import stripe
import json
from django.http import HttpResponse
from django.conf import settings


@login_required
def purchase_checkout(request, program_id):
    '''
    return purchase checkout page 
    '''
    profile = get_object_or_404(Profile, user=request.user)
    program = get_object_or_404(Programs, pk=program_id)
    form = CheckoutForm()
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe.api_key = settings.STRIPE_SECRET_KEY 

    try: 
        stripe.PaymentIntent.create(
            amount = int(program.price),
            currency = 'eur'
        )

    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be processed!')
        return HttpResponse(content=e, status=400)

    context = {
        'form': form,
        'profile': profile,
        'program': program,
        'stripe_public_key': stripe_public_key
    }
    return render(request, 'purchase/purchase_checkout.html', context)

