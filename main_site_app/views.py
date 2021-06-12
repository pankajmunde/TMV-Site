from django.shortcuts import render
from .models import *
import admission_app.models as adm
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def home_view(request):
    events = AddEvents.objects.all()
    teachers = ExpertTeachers.objects.all()
    coming_evnt = UpcomingEvent.objects.all().first()

    return render(request, 'index-2.html', {"events": events, "teachers":teachers, "coming_evnt":coming_evnt})


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
    about = AboutInfo.objects.all().first()

    return render(request, 'about.html', {"teachers":teachers, "about":about})


def events_view(request):
    events = AddEvents.objects.all()

    return render(request, 'event.html', {"events": events})


def contact_view(request):
    if request.method == "POST":

        subject = request.POST.get("subject")
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        description = f"Name : {name}\nEmail: {email}\nMessage:\n\t{message}"

        send_mail(subject, description, settings.EMAIL_HOST_USER, [settings.EMAIL_THIRD_PARTY], fail_silently=False)

        return HttpResponse(f"Email Sent Successfully<hr><br>We will get back to you soon. Thank You!!<br>Go to <a href='/'>Home</a>")
    return render(request, 'contact.html')


# Create your views here.
@login_required
def student_list(request):
    if request.user.is_admin:
        students = [ obj for obj in adm.StorePrimaryAdmissionFormDetails.objects.all() if obj.student_name ]
        fees_data = adm.FeesRecord.objects.all()
        paginator = Paginator(students, 10)
        page = request.GET.get('page')
        paged_students = paginator.get_page(page)

        context = {
            "students": paged_students,
            "fees_data": fees_data
        }
        return render(request, "students/student_list.html", context)
    else:

        return HttpResponse('Access Denied! \n Contact your Admin for Access...  <a href="/accounts/logout/">Logout</a>')