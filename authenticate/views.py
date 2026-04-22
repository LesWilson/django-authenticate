from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'authenticate/index567.html')

def profile(request): 
    return render(request, 'authenticate/profile.html', {})

# don't call login as will clash with core login method
def login_user(request): 

    # determine what request is being received
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            messages.success(request, "You have been logged in", extra_tags="alert alert-success")
            return redirect('home')
     
        else:
            messages.error(request, message="Invalid login.  Please try again.", extra_tags="alert alert-danger text-center")

    return render(request, 'authenticate/login.html')
