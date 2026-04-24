from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Society

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        exclude = ['password',]

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        #we don't want the password on the form
        self.fields.pop('password')

        setFieldFormatting(self)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'First Name'}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        setFieldFormatting(self)

class SocietyForm(ModelForm):
    class Meta:
         model = Society
         fields = ["id", "name", "description", "location"]

    def __init__(self, *args, **kwargs):
        super(SocietyForm, self).__init__(*args, **kwargs)

        setFieldFormatting(self)        


def setFieldFormatting(target):
    
    for field in target.fields:
        target.fields[field].widget.attrs['placeholder'] = ' '
        target.fields[field].widget.attrs['class'] = 'form-control mb-1'
    
    target.label_suffix = ''
    