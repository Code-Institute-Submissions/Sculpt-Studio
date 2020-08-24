from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserManagementForm
from django.contrib import messages
from django.contrib.auth.models import User


@login_required
def account(request):
    """render my_profile.html and handle profile update """
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, f'Profile has been updated!')
            return redirect(reverse('account'))
    else:
        user_form = UserForm(instance=request.user)

    context = {
        'user_form': user_form
    }

    return render(request, 'user_profile/my_account.html', context)


@login_required
def user_management(request):
    """user management view to allow managing users in template view"""
    if request.user.is_superuser:
        if request.method == 'POST':
            form = UserManagementForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect(reverse('account'))
        else:
            form = UserManagementForm(instance=request.user)
    else:
        messages.error(request, f'You must be and administrative user to use this function')
        return redirect(reverse('home'))

    context = {
        'form': form
    }

    return render(request, 'user_profile/user_management.html', context)