from django.shortcuts import render

# Create your views here.

def index(request):
    """
    renders index.html
    """
    return render(request, 'home/index.html')

def about_me(request):
    """
    renders about-me.html
    """
    return render(request, 'home/about-me.html')