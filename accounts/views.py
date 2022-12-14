from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserLoginForm, CustomUserChangeForm, UserProfileForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import (
    CreateView,

)
from django.views.generic import (
    DetailView,
)
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
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


class UserPasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:user_profile')
    success_message = 'Password Changed Successfully'


class UserPasswordResetView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_message = 'Instruction and link has been sent to your email'
    success_url = reverse_lazy('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('manager:index')
        return super(UserPasswordResetView, self).dispatch(request, *args, **kwargs)


class UserPasswordRestConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_message = 'Password Reset Successfull'
    success_url = reverse_lazy('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('manager:index')
        return super(UserPasswordRestConfirmView, self).dispatch(request, *args, **kwargs)


class UserProfileUpdate(LoginRequiredMixin, View):
    template_name = 'accounts/user_profile_update.html'

    def get(self, request, *args, **kwargs):
        user_form = CustomUserChangeForm(instance = request.user)
        profile_form = UserProfileForm(instance = request.user.profile)
        context = {'user_form':user_form, 'profile_form':profile_form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('accounts:user_profile')
        else:
            user_form = CustomUserChangeForm(instance=request.user)
            profile_form = UserProfileForm(instance=request.user.profile)
        return render(request, self.template_name, context={'user_form':user_form, 'profile_form':profile_form})
        