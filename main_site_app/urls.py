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
    path('gallery/', gallery_view, name='gallery'),
    path('sportday/', sports_view, name='sportday'),
    path('wari/', wari_view, name='wari'),
    path('yoga/', yoga_view, name='yoga'),
    path('navratri/', navratri_view, name='navratri'),
    path('dushera/', dushera_view, name='dushera'),
    path('holi/', holi_view, name='holi'),
    path('funfair/', funfair_view, name='funfair'),
    path('ganpati/', ganpati_view, name='ganpati'),
    path('gathering/', gathering_view, name='gathering'),
    path('chrismas/', chrismas_view, name='chrismas'),
    path('donation/', donation_view, name='donation'),
    path('janmastami/', janmastami_view, name='janmastami'),
    path('other/', other_view, name='other'),

]