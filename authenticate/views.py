from django.shortcuts import render

# Create your views here.

def home(request): 
    return render(request, 'authenticate/index.html', {})

def profile(request): 
    return render(request, 'authenticate/profile.html', {})
