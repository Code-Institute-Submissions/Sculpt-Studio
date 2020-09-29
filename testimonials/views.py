from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import AddTestimonialsForm
from .models import Testimonials
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def testimonials(request):
    """
    return all testimonial for template
    """
    testimonials = Testimonials.objects.all()
    
    context = {
        'testimonials': testimonials
    }

    return render(request, 'testimonials/testimonials.html', context)


@login_required
def add_testimonial(request):
    '''form for user to add testimonials'''
    if request.method == 'POST':
        form = AddTestimonialsForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, f'Your review has been succesfully stored')
            return redirect(reverse('testimonials'))
    else:
        form = AddTestimonialsForm()

    context = {
        'form': form
    }

    return render(request, 'testimonials/add_testimonials.html', context) 

@login_required
def delete_testimonials(request, testimonial_id):
    '''allow admin user to delete inappropriate testimonials'''
    testimonial = get_object_or_404(Testimonials, pk=testimonial_id)

    if not request.user.is_superuser:
        messages.error(request, f'You must be and administrative user to use this function')
        return redirect(reverse('home'))
    
    testimonial.delete()

    return redirect(reverse('testimonials'))

