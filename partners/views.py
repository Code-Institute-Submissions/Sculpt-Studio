from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def edit_partners(request, partner_id):
    """
    renders edit page for partners for admin user
    to be able to edit / delete partner details
    """
    partners = get_object_or_404(Partners, pk=partner_id)

    if not request.user.is_superuser:
        messages.error(request, f'You must be and administrative user to use this function')
        return redirect(reverse('partners'))


    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=partners)
        if form.is_valid:
            form.save()
            return redirect(reverse('partners'))
    else:
        form = PartnerForm(instance=partners)

    context = {
        'partners': partners,
        'form': form
    }

    return render(request, 'partners/edit_partners.html', context)



@login_required
def delete_partners(request, partner_id):
    """
    allow admin user to delete specific programs from 
    template view instead of admin tool
    """

    partners = get_object_or_404(Partners, pk=partner_id)

    if not request.user.is_superuser:
        messages.error(request, f'You must be and administrative user to use this function')
        return redirect(reverse('account'))


    partners.delete()

    return redirect(reverse('partners'))