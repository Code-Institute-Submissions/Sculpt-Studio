from django.shortcuts import render, get_object_or_404, redirect
from programs.models import Programs
from django.contrib import messages


def cart(request):
    '''
    return shopping cart 
    '''

    return render(request, 'cart/cart.html')


def add_to_cart(request, program_id):
    '''
    choose program to purhcase and add to cart 
    function
    '''
    program = get_object_or_404(Programs, program_id)
    cart = request.session.get('cart', {})
    cart.pop(program.id)
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect('cart')