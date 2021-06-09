from django.db import models
from django.utils.timezone import now

# Create your models here.

class StorePrimaryAdmissionFormDetails(models.Model):
    username = models.CharField(max_length=255)
    form_type = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=now)
    email = models.EmailField()
    admission_std = models.CharField(max_length=255, null=True)
    dob = models.CharField(max_length=255, null=True)
    student_surname = models.CharField(max_length=255, null=True)
    student_name = models.CharField(max_length=255, null=True)
    student_father_name = models.CharField(max_length=255, null=True)
    student_category = models.CharField(max_length=255, null=True)
    student_caste = models.CharField(max_length=255, null=True)
    student_gender = models.CharField(max_length=255, null=True)
    student_religion = models.CharField(max_length=255, null=True)
    student_blood_group = models.CharField(max_length=255, null=True)
    student_present_addr = models.CharField(max_length=255, null=True)
    student_telephone = models.CharField(max_length=12, null=True)
    student_mobile = models.CharField(max_length=12, null=True)
    student_previous_school = models.CharField(max_length=255, null=True)
    student_previous_class = models.CharField(max_length=255, null=True)
    student_previous_medium = models.CharField(max_length=255, null=True)
    student_close_landmark = models.CharField(max_length=255, null=True)
    student_known_lang = models.CharField(max_length=255, null=True)
    student_allergies = models.CharField(max_length=255, null=True)
    student_alments = models.CharField(max_length=255, null=True)
    student_id_mark = models.CharField(max_length=255, null=True)
    student_home_time = models.CharField(max_length=255, null=True)

    # Family Information

    father_surname = models.CharField(max_length=255, null=True)
    father_name = models.CharField(max_length=255, null=True)
    father_father_name = models.CharField(max_length=255, null=True)
    father_age = models.CharField(max_length=3, null=True)
    father_education = models.CharField(max_length=255, null=True)
    father_work_and_addr = models.CharField(max_length=255, null=True)
    father_designation = models.CharField(max_length=255, null=True)
    father_income = models.CharField(max_length=10, null=True)
    father_telephone = models.CharField(max_length=12, null=True)
    father_mobile = models.CharField(max_length=12, null=True)

    mother_surname = models.CharField(max_length=255, null=True)
    mother_name = models.CharField(max_length=255, null=True)
    mother_father_name = models.CharField(max_length=255, null=True)
    mother_age = models.CharField(max_length=3, null=True)
    mother_education = models.CharField(max_length=255, null=True)
    mother_work_and_addr = models.CharField(max_length=255, null=True)
    mother_designation = models.CharField(max_length=255, null=True)
    mother_income = models.CharField(max_length=10, null=True)
    mother_telephone = models.CharField(max_length=12, null=True)
    mother_mobile = models.CharField(max_length=12, null=True)

    emargency_contact = models.CharField(max_length=12, null=True)
    single_parent = models.CharField(max_length=255, null=True)
    family_type = models.CharField(max_length=255, null=True)
    family_members = models.CharField(max_length=3, null=True)
    siblings = models.CharField(max_length=255, null=True)
    sibling1_name = models.CharField(max_length=255, null=True)
    sibling1_age = models.CharField(max_length=3, null=True)
    sibling1_school = models.CharField(max_length=255, null=True)
    sibling2_name = models.CharField(max_length=255, null=True)
    sibling2_age = models.CharField(max_length=3, null=True)
    sibling2_school = models.CharField(max_length=255, null=True)

    bus_route_num = models.CharField(max_length=4, null=True)
    bus_stop = models.CharField(max_length=255, null=True)

    # documents upload
    student_photo = models.FileField(upload_to='Student_photos/')
    birth_certificate = models.FileField(upload_to='Birth_certificates/')
    student_adhaar_card = models.FileField(upload_to='Adhaar_cards/')
    blood_group_certificate = models.FileField(upload_to='Blood_group_certificates/')
    fitness_certificate = models.FileField(upload_to='Fitness_certificates/')
    parent_photo = models.FileField(upload_to='Parent_photos/')
    transfer_certificate = models.FileField(upload_to='Transfer_certificates/')
    report_card = models.FileField(upload_to='Report_cards/')
    caste_certificate = models.FileField(upload_to='Caste_certificates/')
    electricity_bill = models.FileField(upload_to='Electricity_bill/')

    def __str__(self):
        return f"{self.student_surname} {self.student_name} {self.student_father_name}"
