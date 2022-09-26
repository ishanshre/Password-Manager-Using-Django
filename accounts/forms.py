from email.policy import default
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.views import AuthenticationForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['first_name','last_name','age','nickname','username','email']


class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','age','nickname','username','email']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=20, label='',widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(max_length=20, label='',widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = get_user_model()
        fields = ['username','password','remember_me']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar','body','address']
        