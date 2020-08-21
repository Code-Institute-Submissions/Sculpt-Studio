from django.shortcuts import render

# Create your views here.

def programs(request):
    """
    render programs.html
    """
    return render(request, 'programs/programs.html')