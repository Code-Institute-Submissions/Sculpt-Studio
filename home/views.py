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


#custom error views 

def server_error(request):
    """
    handle 500 error
    """
    return(request, '500.html')

def not_found(request, exception):
    """
    handle 404 error
    """
    return(request, '404.html')