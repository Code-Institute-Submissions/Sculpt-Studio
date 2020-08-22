from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Programs
from .forms import ProgramForm



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


def edit_program(request, program_id):
    """
    renders edit pagefor specific program
    """
    programs = get_object_or_404(Programs, pk=program_id)

    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=programs)
        if form.is_valid:
            form.save()
            return redirect(reverse('program_details', args=[programs.id]))
    else:
        form = ProgramForm(instance=programs)

    context = {
        'programs': programs,
        'form': form
    }

    return render(request, 'programs/edit_program.html', context)
