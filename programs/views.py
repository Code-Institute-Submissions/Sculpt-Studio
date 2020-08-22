from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Programs
from .forms import ProgramForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



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


@login_required
def edit_program(request, program_id):
    """
    renders edit pagefor specific program
    """
    programs = get_object_or_404(Programs, pk=program_id)

    if not request.user.is_superuser:
        messages.error(request, f'You must be and administrative user to use this function')
        return redirect(reverse('home'))


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


@login_required
def delete_program(request, program_id):
    """
    delete specific program
    """

    programs = get_object_or_404(Programs, pk=program_id)

    if not request.user.is_superuser:
        messages.error(request, f'You must be and administrative user to use this function')
        return redirect(reverse('home'))


    programs.delete() 

    return redirect(reverse('programs'))



@login_required
def add_program(request):
    """
    allow admin users to add new programs program
    """

    if not request.user.is_superuser:
        messages.error(request, f'You must be and administrative user to use this function')
        return redirect(reverse('home'))


    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid:
            program = form.save()
            return redirect(reverse('program_details', args=[program.id]))
    else:
        form = ProgramForm()

    context = {
        'form': form
    }

    return render(request, 'programs/add_programs.html', context)