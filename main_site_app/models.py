from django.db import models
from django.utils.timezone import now


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