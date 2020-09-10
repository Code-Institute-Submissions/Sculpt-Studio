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
    program = request.POST.get('add')
    cart = request.session.get('cart', {})

    if program_id in list(cart.keys()):
        messages.error(request, 'This programs is already chosen for purchase')
    else: 
        cart[program_id] = program

    request.session['cart'] = cart
    print(request.session['cart'])



    return redirect('cart')