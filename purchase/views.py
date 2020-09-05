from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CheckoutForm

@login_required
def purchase_checkout(request):
    '''
    return purchase checkout page 
    '''
    
    form = CheckoutForm()


    context = {
        'form': form
    }
    return render(request, 'purchase/purchase_checkout.html', context)

