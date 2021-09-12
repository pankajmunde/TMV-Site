from django.contrib import admin
from .models import *

# Register your models here.
class StorePrimaryAdmissionFormDetailsAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super(StorePrimaryAdmissionFormDetailsAdmin, self).get_form(request, obj, **kwargs)
        for key in form.base_fields.keys():
            form.base_fields[key].required = False
        return form

admin.site.site_header = 'TMV Administration'
admin.site.register(StorePrimaryAdmissionFormDetails, StorePrimaryAdmissionFormDetailsAdmin)
admin.site.register(FeesRecord)