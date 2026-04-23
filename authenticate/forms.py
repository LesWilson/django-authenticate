from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class EditProfileForm(UserChangeForm):

    # password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        exclude = ['password',]

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields.pop('password')
        self.label_suffix = ''
        self.fields['username'].widget.attrs['class'] = 'form-control mb-1'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = 'Username'

        # self.fields['password'].widget.attrs['class'] = 'form-control mb-1'
        # self.fields['password'].widget.attrs['placeholder'] = ''
        # self.fields['password'].label = ''
        # self.fields['password'].help_text = ''

        self.fields['first_name'].widget.attrs['class'] = 'form-control mb-1'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = 'First Name'

        self.fields['last_name'].widget.attrs['class'] = 'form-control mb-1'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = 'Last Name'

        self.fields['email'].widget.attrs['class'] = 'form-control mb-1'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = 'Email'



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'First Name'}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.label_suffix = ''
        self.fields['username'].widget.attrs['class'] = 'form-control mb-1'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = 'Username'

        self.fields['password1'].widget.attrs['class'] = 'form-control mb-1'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = 'Password'
        # self.fields['password1'].help_text = self.fields['password1'].help_text.replace("<ul>", "<ul class='helptext'>")

        self.fields['password2'].widget.attrs['class'] = 'form-control mb-1'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = 'Confirm Password'

