from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserLoginForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import (
    CreateView,

)
from django.views.generic import (
    DetailView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
# Create your views here.


class UserSignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_message = 'User Successfully Created'
    success_url = reverse_lazy('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('manager:index')
        return super(UserSignUpView, self).dispatch(request, *args, **kwargs)

class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    success_message = "Successfull Login"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('manager:index')
        return super(UserLoginView, self).dispatch(request,*args, **kwargs)
    

class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'accounts/user_profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
