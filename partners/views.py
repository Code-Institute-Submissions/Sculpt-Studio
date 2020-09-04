from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Partners
from .forms import PartnerForm

def partners(request):
    '''all partners view'''

    partners = Partners.objects.all()

    context = {
        'partners': partners
    }
        
    
    return render(request, 'partners/partners.html', context)


@login_required
def add_partners(request):
    '''add partners functionality for admin users'''

    if not request.user.is_superuser:
        messages.error(request, f'You must be and administrative user to use this function')
        return redirect(reverse('partners'))


    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(reverse('partners'))
    else:
        form = PartnerForm()

    context = {
        'form': form
    }

    return render(request, 'partners/add_partners.html', context)