from django.shortcuts import render,redirect,reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserManagementForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


@login_required
def account(request):
    """render my_profile.html and handle profile update """
    user_profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user_profile)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, f'Profile has been updated!')
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
        else:
            form = UserManagementForm(instance=request.user)
    else:
        messages.error(request, f'You must be and administrative user to use this function')
        return redirect(reverse('home'))

    context = {
        'form': form
    }

    return render(request, 'user_profile/user_management.html', context)