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


def program_details(request, program_id):
    """
    renders details about specific fitness program
    """
    programs = get_object_or_404(Programs, pk=program_id)

    context = {
        'programs': programs
    }

    return render(request, 'programs/program_details.html', context)