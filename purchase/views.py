from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CheckoutForm
from programs.models import Programs
from user_profile.models import Profile
from .models import Checkout, CheckoutLineItem
from django.contrib.auth.models import User
import stripe
import json
from django.conf import settings
from cart.contexts import cart_content


@login_required
def purchase_checkout(request):
    '''
    return purchase checkout page and handle 
    taking payment info / creating payment intent with stripe
    '''
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY



    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        cart = request.session.get('cart', {})
        if form.is_valid:
            order = form.save(commit=False)
            order.original_cart = json.dumps(cart)
            order = form.save()
            for program_id, program_data in cart.items():
                    program = Programs.objects.get(id=program_id)
                    checkout_line_item = CheckoutLineItem(
                        purchase=order,
                        program=program,
                        quantity=program_data
                        )
                    checkout_line_item.save()
            return redirect(reverse('purchase_successful', args=[order.order_number]))
        else: 
            messages.error(request, f'An error occured!')
    else:
        cart_now = cart_content(request)
        cost = cart_now['total']
        stripe_cost = round(cost * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount = stripe_cost,
            currency = settings.STRIPE_CURRENCY

        )

    if request.user.is_authenticated:
        '''
        prefill form for logged in user
        '''
        try:
            profile = Profile.objects.get(user=request.user)
            form = CheckoutForm(initial={
                'user': profile.user,
                'country': profile.country,
                'email': profile.user.email,
                'billing_address': profile.address,
                'billing_country': profile.country,
            })
        except Profile.DoesNotExist:
            form = CheckoutForm()
    else:
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

    purchase = get_object_or_404(Checkout, order_number=order_number)

    if request.user.is_authenticated: 
        profile = get_object_or_404(Profile, user=request.user)
        purchase.user = profile
        purchase.save()

    messages.success(request, f'Thank you for your purchase!\
                                You can view your order details by checking your account.')


    if 'cart' in request.session:
        del request.session['cart']


    context = {
        'purchase': purchase,
    }

    return render(request, 'purchase/purchase_successful.html', context)


def user_purchases(request, user_id):
    '''
    render user purchase history in 
    account section 
    '''

    profile = get_object_or_404(Profile, user_id=request.user)
    purchase = Checkout.objects.filter(user=profile)
 

    context = {
        'profile': profile,
        'purchase': purchase

    }

    return render(request, 'purchase/user_purchases.html', context)