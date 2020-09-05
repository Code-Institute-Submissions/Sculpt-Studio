from django.shortcuts import render


def cart(request):
    '''
    return shopping cart 
    '''

    return render(request, 'cart/cart.html')
