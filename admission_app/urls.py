from django.urls import path
from .views import *

app_name = 'admission_app'

urlpatterns = [
    path('', admissions_view, name='admissions'),
    path('application-list/', AdmissionApplicationView.as_view(), name='application-list'),
    path('primary-form/', admissions_view, name='primary-form'),
    path('generate-pdf/<int:pk>/', GeneratePdf.as_view(), name='pdf-application-view'),
]