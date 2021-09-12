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

def gallery_view(request):

    return render(request, 'Gallary.html')


def sports_view(request):
    gallery = Gallery.objects.filter(title="Sports Day").first()
    obj = GalleryImage.objects.filter(gallery=gallery)
    images = [i.images for i in obj]
    return render(request, 'sportday.html', {"images":images})

def wari_view(request):
    gallery = Gallery.objects.filter(title="wari").first()
    obj = GalleryImage.objects.filter(gallery=gallery)
    images = [i.images for i in obj]
    return render(request, 'wari.html', {"images":images})

def yoga_view(request):
    gallery = Gallery.objects.filter(title="yoga").first()
    obj = GalleryImage.objects.filter(gallery=gallery)
    images = [i.images for i in obj]
    return render(request, 'Yoga.html', {"images":images})

def navratri_view(request):
    gallery = Gallery.objects.filter(title="navratri").first()
    obj = GalleryImage.objects.filter(gallery=gallery)
    images = [i.images for i in obj]
    return render(request, 'navratri.html', {"images":images})


def dushera_view(request):
    gallery = Gallery.objects.filter(title="dushera").first()
    obj = GalleryImage.objects.filter(gallery=gallery)
    images = [i.images for i in obj]
    return render(request, 'Dusshra.html', {"images":images})

def holi_view(request):
    gallery = Gallery.objects.filter(title="holi").first()
    obj = GalleryImage.objects.filter(gallery=gallery)
    images = [i.images for i in obj]
    return render(request, 'Holi.html', {"images":images})

def funfair_view(request):
    gallery = Gallery.objects.filter(title="funfair").first()
    obj = GalleryImage.objects.filter(gallery=gallery)
    images = [i.images for i in obj]
    return render(request, 'funfair.html', {"images":images})

def ganpati_view(request):
    gallery = Gallery.objects.filter(title="ganpati").first()
    obj = GalleryImage.objects.filter(gallery=gallery)
    images = [i.images for i in obj]
    return render(request, 'ganpati.html', {"images":images})

def gathering_view(request):
    gallery = Gallery.objects.filter(title="Gathering").first()
    obj = GalleryImage.objects.filter(gallery=gallery)
    images = [i.images for i in obj]
    return render(request, 'Gathering.html', {"images":images})

def chrismas_view(request):
    gallery = Gallery.objects.filter(title="cristmas").first()
    obj = GalleryImage.objects.filter(gallery=gallery)
    images = [i.images for i in obj]
    return render(request, 'cristmas.html', {"images":images})

def donation_view(request):
    gallery = Gallery.objects.filter(title="donation").first()
    obj = GalleryImage.objects.filter(gallery=gallery)
    images = [i.images for i in obj]
    return render(request, 'donation.html', {"images":images})

def janmastami_view(request):
    gallery = Gallery.objects.filter(title="janmastmi").first()
    obj = GalleryImage.objects.filter(gallery=gallery)
    images = [i.images for i in obj]
    return render(request, 'janmastmi.html', {"images":images})

def other_view(request):
    gallery = Gallery.objects.filter(title="other").first()
    obj = GalleryImage.objects.filter(gallery=gallery)
    images = [i.images for i in obj]
    return render(request, 'other.html', {"images":images})

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