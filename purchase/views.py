from django.shortcuts import render

from django.shortcuts import render


def purchase_checkout(request):
    '''
    return purchase checkout page 
    '''

    return render(request, 'purchase/purchase_checkout.html')

