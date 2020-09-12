from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CheckoutForm
from user_profile.models import Profile
from programs.models import Programs
from .models import Checkout
from django.contrib.auth.models import User
import stripe
import json
from django.http import HttpResponse
from django.conf import settings
from cart.contexts import cart_content


@login_required
def purchase_checkout(request):
    '''
    return purchase checkout page 
    '''
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    profile = get_object_or_404(Profile, user=request.user)
    cart = request.session.get('cart', {})




    if request.method == 'POST':

        cart = request.session.get('cart', {})
        form = CheckoutForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you for your purchase, a confirmation email will be sent to your'
                                        'registered email address! You can also check your purchases from your profile')
        else: 
            messages.error(request, f'An error occured!')
        return redirect(reverse('purchase_successful'))
    else:
        cart_now = cart_content(request)
        cost = cart_now['total']
        stripe_cost = round(cost * 100)
        stripe.api_key = stripe_secret_key
        cart = json.dumps(cart)
        intent = stripe.PaymentIntent.create(
            amount = stripe_cost,
            currency = settings.STRIPE_CURRENCY

        )
        form = CheckoutForm()


    context = {
        'form': form,
        'profile': profile,
        'cart': cart_now,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }
    return render(request, 'purchase/purchase_checkout.html', context)


@login_required
def purchase_successful(request):
    '''
    render after successful purchase action
    '''
    order_number = get_object_or_404(Checkout)
    profile = get_object_or_404(Profile, user=request.user)

    context = {
        'purchase': order_number,
        'profile': profile,
    }

    return render(request, 'purchase/purchase_successful.html', context)