from django.shortcuts import render
from .models import *


# Create your views here.
def home_view(request):
    events = AddEvents.objects.all()
    teachers = ExpertTeachers.objects.all()

    return render(request, 'index-2.html', {"events": events, "teachers":teachers})


def attendance_view(request):
    return render(request, 'school_one.html')


def parents_participation_view(request):
    return render(request, 'school_two.html')


def general_rules_view(request):
    return render(request, 'school_three.html')


def holiday_list_view(request):
    return render(request, 'school_four.html')


def about_view(request):
    teachers = ExpertTeachers.objects.all()

    return render(request, 'about.html', {"teachers":teachers})


def events_view(request):
    events = AddEvents.objects.all()
    return render(request, 'event.html', {"events": events})


def contact_view(request):
    return render(request, 'contact.html')
