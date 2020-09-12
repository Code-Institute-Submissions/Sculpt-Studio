from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CheckoutForm
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
    profile = get_object_or_404(User, user=request.user)
    cart = request.session.get('cart', {})




    if request.method == 'POST':

        cart = request.session.get('cart', {})
        form = CheckoutForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
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
def purchase_successful(request, order_number):
    '''
    render after successful purchase action
    '''
    profile = get_object_or_404(User, user=request.user)
    purchase = get_object_or_404(Checkout, order_number=order_number)

    messages.success(request, f'Thank you for your purchase!\
                                You will receive a confirmation via your e-mail provided during your order.\
                                Your order number is { purchase.order_number }!')


    if 'cart' in request.session:
        del request.session['cart']


    context = {

        'profile': profile,
        'purchase': purchase,
    }

    return render(request, 'purchase/purchase_successful.html', context)