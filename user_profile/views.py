from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def account(request):
    """render my_profile.html"""

    return render(request, 'user_profile/my_account.html')
