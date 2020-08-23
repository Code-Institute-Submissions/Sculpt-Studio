from django.shortcuts import render

# Create your views here.

def my_profile(request):
    """render my_profile.html"""

    return render(request, 'user_profile/my_profile.html')
