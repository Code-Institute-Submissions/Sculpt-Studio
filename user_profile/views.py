from django.shortcuts import render,redirect,reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserManagementForm
from purchase.models import Checkout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.db.models import Q


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
def user_selection(request):
    """get all users to choose by admin for updating"""
    if not request.user.is_superuser:
            messages.error(request, f'You must be and administrative user to use this function')
            return redirect(reverse('home'))
    users = User.objects.all()
    search = ''

    '''code institute project code and help from stackoverflow used as inspiration in solving below search function'''
    if 'search' in request.GET:
        search = request.GET['search']
        if not search:
            messages.error(request, f'No valid search criteria entered!')
            return redirect(reverse('user_selection'))

        results = Q(first_name__icontains=search) | Q(last_name__icontains=search) | Q(username__icontains=search)
        users = users.filter(results)
        

    context = {
        'users': users,
        'find_user': search,
    }
    return render(request, 'user_profile/user_selection.html', context)


@login_required
def user_management(request, user_id):
    """user management view to allow managing users in template view"""
    profile = get_object_or_404(User, pk=user_id)

    if not request.user.is_superuser:
            messages.error(request, f'You must be and administrative user to use this function')
            return redirect(reverse('home'))

    if request.method == 'POST':
        form = UserManagementForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile has been updated!')
    else:
        form = UserManagementForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'user_profile/user_management.html', context)


@login_required
def book_meeting(request, user_id):
    """
    render book_meeting.html where calendly booking widget is embedded
    if user has purchases
    """
    user = get_object_or_404(Profile, user_id=request.user)
    purchases = Checkout.objects.filter(user=user)

    context = {
        'user': user,
        'purchases': purchases
    }
    return render(request,'user_profile/book_meeting.html', context)


