from django.db import models
from django.utils.timezone import now


class Gallery(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(blank=True)

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.gallery.title


# Create your models here.
class AddEvents(models.Model):
    created_date = models.DateTimeField(default=now)
    event_title = models.CharField(max_length=1000)
    event_date = models.DateField()
    event_location = models.CharField(max_length=1000)
    event_photo = models.FileField(upload_to='Event_photos/')
    event_info = models.TextField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.event_title



class ExpertTeachers(models.Model):
    created_date = models.DateTimeField(default=now)
    name = models.CharField(max_length=255)
    photo = models.FileField(upload_to='Staff_photos/')
    experties = models.CharField(max_length=255)
    is_active = models.BooleanField()


    def __str__(self):
        return self.name


class UpcomingEvent(models.Model):
    created_date = models.DateTimeField(default=now)
    event_date = models.DateField()
    event_title = models.CharField(max_length=500)
    event_info = models.TextField()
    event_poster = models.FileField(upload_to='Event_poster/')

    def __str__(self):
        return self.event_title


class AboutInfo(models.Model):
    created_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=500)
    photo = models.FileField(upload_to="About_photos/")
    description = models.TextField()
    chairman_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title
