from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views



app_name = 'accounts'

urlpatterns = [
    path('register/', CustomerRegister.as_view(), name='register'),
    # path('login/', login_request, name='login'),
    path('login/', login_request, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('change-password/', auth_views.PasswordChangeView.as_view()),
    # path('password_reset/', auth_views.PasswordResetView.as_view()),
    # path('password_reset_confirm/', auth_views.PasswordResetConfirmView.as_view()),
    # path('password_reset_done/', auth_views.PasswordChangeDoneView.as_view()),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view()),

]