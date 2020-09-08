from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CheckoutForm
from user_profile.models import Profile
from programs.models import Programs
from django.contrib.auth.models import User
import stripe
from django.http import HttpResponse
from django.conf import settings



@login_required
def purchase_checkout(request, program_id):
    '''
    return purchase checkout page 
    '''
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    profile = get_object_or_404(Profile, user=request.user)
    program = get_object_or_404(Programs, pk=program_id)
    form = CheckoutForm(request.POST) 
    cost = program.price
    stripe_cost = round(cost * 100)
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_cost,
        currency=settings.STRIPE_CURRENCY
    )

    print (intent)


    context = {
        'form': form,
        'profile': profile,
        'program': program,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }
    return render(request, 'purchase/purchase_checkout.html', context)

