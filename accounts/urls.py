from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('register/', CustomerRegister.as_view(), name='register'),
    # path('login/', login_request, name='login'),
    path('login/', login_request, name='login'),
    path('logout/', logout_view, name='logout'),
]