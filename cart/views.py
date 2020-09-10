from django.shortcuts import render, get_object_or_404, redirect, reverse
from programs.models import Programs
from django.contrib import messages



def cart(request):
    '''
    display shopping cart to customers after program chosen
    for purchase
    '''

    return render(request, 'cart/cart.html')


def add_to_cart(request, program_id):
    '''
    adding programs chosen to purchase to
    cart before payment

    '''
    cart = request.session.get('cart', {})
    program_count = 1

    if program_id in list(cart.keys()):
        messages.error(request, f'This programs is already chosen for purchase')
    else: 
        cart[program_id] = program_count

    request.session['cart'] = cart



    return redirect(reverse('cart'))


def remove_from_cart(request):
    '''
    removing added program from cart 
    '''

    cart = request.session.get('cart', {})
    cart.clear()
    messages.success(request, f'Program removed from cart!')


    return redirect(reverse('programs'))