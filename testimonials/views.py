from django.shortcuts import render, get_object_or_404
from .forms import AddTestimonialsForm
from .models import Testimonials


def testimonials(request):
    
    
    if request.method == 'POST':
        form = AddTestimonialsForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = AddTestimonialsForm()
    
    context = {
        'form': form
    }

    return render(request, 'testimonials/testimonials.html', context)
