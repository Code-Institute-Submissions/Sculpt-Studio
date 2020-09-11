from django.shortcuts import render, get_object_or_404, redirect, reverse
from programs.models import Programs
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def cart(request):
    '''
    display shopping cart to customers after program chosen
    for purchase
    '''

    return render(request, 'cart/cart.html')

@login_required
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

@login_required
def remove_from_cart(request, program_id):
    '''
    removing added program from cart 
    '''
    program = get_object_or_404(Programs, pk=program_id)
    cart = request.session.get('cart', {})
    id = str(program_id)
    cart.pop(id)
    messages.success(request, f'{program.name} succesfully removed from your shopping cart!')

    request.session['cart'] = cart

    return redirect(reverse('cart'))