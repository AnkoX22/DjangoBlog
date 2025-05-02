from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Tailwind classes to all fields
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({
                'class': 'border border-gray-900 px-1 py-1 max-w-md focus:outline-none focus:ring-1 focus:ring-blue-500',
            })


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Tailwind classes to all fields
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({
                'class': 'border border-gray-900 px-1 py-1 max-w-md focus:outline-none focus:ring-1 focus:ring-blue-500',
            })


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Username',
                                   'class': 'form-control',
                               }))

    password = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                       'placeholder': 'Password',
                                       'class': 'form-control',
                                       'data-toggle': 'password',
                                       'id': 'password',
                                       'name': 'password',
                                }))

    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Tailwind classes to all fields
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({
                'class': 'border border-gray-900 px-1 py-1 max-w-md focus:outline-none focus:ring-1 focus:ring-blue-500',
            })


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                              'class': 'form-control',
                                                              })
                                 )
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Last Name',
                                    'class': 'form-control',
                                }))

    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Username',
                                   'class': 'form-control',
                               }))

    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Email',
                                 'class': 'form-control',
                             }))

    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Password',
                                    'class': 'form-control',
                                    'data-toggle': 'password',
                                    'id': 'password',
                                }))

    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Confirm Password',
                                    'class': 'form-control',
                                    'data-toggle': 'password',
                                    'id': 'password',
                                }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Tailwind classes to all fields
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({
                'class': 'border border-gray-900 px-1 py-1 max-w-md focus:outline-none focus:ring-1 focus:ring-blue-500',
            })