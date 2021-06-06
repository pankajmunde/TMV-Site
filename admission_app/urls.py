from django.urls import path
from .views import *

app_name = 'admission_app'

urlpatterns = [
    path('', admissions_view, name='admissions'),
    path('application-list/', applications_list_view, name='application-list'),
    path('primary-form/', admissions_view, name='primary-form'),
]