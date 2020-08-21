from django.shortcuts import render, get_object_or_404
from .models import Programs

# Create your views here.

def programs(request):
    """
    render programs.html
    """
    programs = Programs.objects.all()

    context = {
        'programs': programs,
    }

    
    return render(request, 'programs/programs.html', context)