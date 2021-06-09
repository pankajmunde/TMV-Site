from django.urls import path
from .views import *

app_name = 'admission_app'

urlpatterns = [
    path('', primary_admissions_view, name='admissions'),
    path('application-list/', AdmissionApplicationView.as_view(), name='application-list'),
    path('primary-form/', primary_admissions_view, name='primary-form'),
    path('pri-primary/', pre_primary_admissions_view, name='pre-primary-form'),
    path('generate-pdf/<int:pk>/', GeneratePdf.as_view(), name='pdf-application-view'),
]