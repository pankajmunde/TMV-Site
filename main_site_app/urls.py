from django.urls import path
from .views import *

app_name = 'main_site_app'

urlpatterns = [
    path('', home_view, name='home'),
    path('attendance/', attendance_view, name='attendance'),
    path('parents-participantion/', parents_participation_view, name='parents-participantion'),
    path('general-rules/', general_rules_view, name='general-rules'),
    path('holiday-list/', holiday_list_view, name='holiday-list'),
    path('about/', about_view, name='about'),
    path('events/', events_view, name='events'),
    path('contact/', contact_view, name='contact'),
    path('school-admin/', student_list, name='student_list'),

]