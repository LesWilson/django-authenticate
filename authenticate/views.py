from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, password_validation, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView

from .forms import RegistrationForm, EditProfileForm, SocietyForm
from .models import Society


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

def edit_profile(request): 

    # determine what request is being received
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        
            messages.success(request, "You have successfully updated your profile", extra_tags="alert alert-success alert-dismissible fade show")
            return redirect('home')
        
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'authenticate/edit_profile.html', {'form': form})


def change_password(request):
    
    # determine what request is being received
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "You have successfully updated your password", extra_tags="alert alert-success alert-dismissible fade show")
            return redirect('home')
        
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'authenticate/change_password.html', {'form': form})


class SocietyListView(ListView):
    model = Society

    context_object_name = 'society_list'   # your own name for the list as a template variable
    template_name = 'society/list.html'
    paginate_by = 10

class SocietyDetailView(UpdateView):
    model = Society
    template_name = 'society/details.html'
    form_class = SocietyForm
    template_name_suffix = ''
    success_url = "/societies/"

    def form_valid(self, form):
        messages.success(self.request, "The society was updated successfully.", extra_tags="alert alert-success alert-dismissible fade show")
        return super(SocietyDetailView,self).form_valid(form)

