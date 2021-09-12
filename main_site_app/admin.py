from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AddEvents)
admin.site.register(ExpertTeachers)
admin.site.register(UpcomingEvent)
admin.site.register(AboutInfo)


from .models import Gallery, GalleryImage

class GalleyImageAdmin(admin.StackedInline):
    model = GalleryImage

@admin.register(Gallery)
class PostAdmin(admin.ModelAdmin):
    inlines = [GalleyImageAdmin]

    class Meta:
       model = Gallery

@admin.register(GalleryImage)
class GalleyImageAdmin(admin.ModelAdmin):
    pass