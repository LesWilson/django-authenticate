from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, password_validation
from django.utils.html import format_html

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

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

            messages.success(request, "You have been logged in", extra_tags="alert alert-success alert-dismissible fade show")
            return redirect('home')
     
        else:
            messages.error(request, message="Invalid login.  Please try again.", extra_tags="alert alert-danger alert-dismissible fade show text-center")

    return render(request, 'authenticate/login.html')


def logout_user(request): 

    logout(request)

    messages.success(request, "You have been logged out successfully", extra_tags="alert alert-success alert-dismissible fade show")
    return redirect('home')


def register_user(request): 

    # determine what request is being received
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
        
            messages.success(request, "You have successfully registered and been logged in", extra_tags="alert alert-success alert-dismissible fade show")
            return redirect('home')
        
    else:
        form = RegistrationForm()

    return render(request, 'authenticate/register.html', {'form': form})


# manual processing of a registerration request
# def register_user(request): 

#     # determine what request is being received
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         confirmPassword = request.POST['confirmPassword']
#         firstName = request.POST['firstName']
#         lastName = request.POST['lastName']
#         email = request.POST['email']

#         user = User.objects.create_user(username=username, email=email, password=password, first_name=firstName, last_name=lastName)

#         if user is not None:
#             login(request, user)

#             messages.success(request, "You have successfully registered and been logged in", extra_tags="alert alert-success alert-dismissible fade show")
#             return redirect('home')
     
#         else:
#             messages.error(request, message="Invalid information.  Please try again.", extra_tags="alert alert-danger alert-dismissible fade show text-center")

#     return render(request, 'authenticate/register.html')

# messages.debug(request, "%s SQL statements were executed." % count)
# messages.info(request, "Three credits remain in your account.")
# messages.success(request, "Profile details updated.")
# messages.warning(request, "Your account expires in three days.")
# messages.error(request, "Document deleted.")
