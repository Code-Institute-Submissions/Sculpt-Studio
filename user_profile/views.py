from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from .forms import UserForm

# Create your views here.

@login_required
def account(request):
    """render my_profile.html"""

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('account'))
    else:
        user_form = UserForm(instance=request.user)

    context = {
        'user_form': user_form
    }

    return render(request, 'user_profile/my_account.html', context)