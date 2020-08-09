from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Budget


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email...'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username...'}))
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Password...'}))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Verify Password...'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username...'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Password...'}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        exclude = ['user']
