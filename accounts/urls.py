from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('password_change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/confirm/<uidb64>/<token>', views.UserPasswordRestConfirmView.as_view(), name='password_reset_confirm'),
    path('user_profile/update/', views.UserProfileUpdate.as_view(), name='user_profile_update'),
]