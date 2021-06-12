from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import StorePrimaryAdmissionFormDetails

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import View, ListView
from datetime import datetime


# Create your views here.
@login_required
def primary_admissions_view(request):
    # print(request.POST)
    if request.method == 'POST':
        admission_std = request.POST.get("admission_std")
        dob = request.POST.get("dob")
        student_surname = request.POST.get("student_surname")
        student_name = request.POST.get("student_name")
        student_father_name = request.POST.get("student_father_name")
        student_category = request.POST.get("student_category")
        student_caste = request.POST.get("student_caste")
        student_gender = request.POST.get("student_gender")
        student_religion = request.POST.get("student_religion")
        student_blood_group = request.POST.get("student_blood_group")
        student_present_addr = request.POST.get("student_present_addr")
        student_telephone = request.POST.get("student_telephone")
        student_mobile = request.POST.get("student_mobile")
        student_previous_school = request.POST.get("student_previous_school")
        student_previous_class = request.POST.get("student_previous_class")
        student_previous_medium = request.POST.get("student_previous_medium")
        student_close_landmark = request.POST.get("student_close_landmark")
        student_known_lang = request.POST.get("student_known_lang")
        student_allergies = request.POST.get("student_allergies")
        student_alments = request.POST.get("student_alments")
        student_id_mark = request.POST.get("student_id_mark")
        student_home_time = request.POST.get("student_home_time")

        # Family Information

        father_surname = request.POST.get("father_surname")
        father_name = request.POST.get("father_name")
        father_father_name = request.POST.get("father_father_name")
        father_age = request.POST.get("father_age")
        father_education = request.POST.get("father_education")
        father_work_and_addr = request.POST.get("father_work_and_addr")
        father_designation = request.POST.get("father_designation")
        father_income = request.POST.get("father_income")
        father_telephone = request.POST.get("father_telephone")
        father_mobile = request.POST.get("father_mobile")

        mother_surname = request.POST.get("mother_surname")
        mother_name = request.POST.get("mother_name")
        mother_father_name = request.POST.get("mother_father_name")
        mother_age = request.POST.get("mother_age")
        mother_education = request.POST.get("mother_education")
        mother_work_and_addr = request.POST.get("mother_work_and_addr")
        mother_designation = request.POST.get("mother_designation")
        mother_income = request.POST.get("mother_income")
        mother_telephone = request.POST.get("mother_telephone")
        mother_mobile = request.POST.get("mother_mobile")

        emargency_contact = request.POST.get("emargency_contact")
        single_parent = request.POST.get("single_parent")
        family_type = request.POST.get("family_type")
        family_members = request.POST.get("family_members")
        siblings = request.POST.get("siblings")
        sibling1_name = request.POST.get("sibling1_name")
        sibling1_age = request.POST.get("sibling1_age")
        sibling1_school = request.POST.get("sibling1_school")
        sibling2_name = request.POST.get("sibling2_name")
        sibling2_age = request.POST.get("sibling2_age")
        sibling2_school = request.POST.get("sibling2_school")

        bus_route_num = request.POST.get("bus_route_num")
        bus_stop = request.POST.get("bus_stop")

        # documents upload
        student_photo = request.FILES.get("student_photo")
        birth_certificate = request.FILES.get("birth_certificate")
        student_adhaar_card = request.FILES.get("student_adhaar_card")
        blood_group_certificate = request.FILES.get("blood_group_certificate")
        fitness_certificate = request.FILES.get("fitness_certificate")
        parent_photo = request.FILES.get("parent_photo")
        transfer_certificate = request.FILES.get("transfer_certificate")
        report_card = request.FILES.get("report_card")
        caste_certificate = request.FILES.get("caste_certificate")
        electricity_bill = request.FILES.get("electricity_bill")

        # print(request.POST)
        # print(request.FILES)

        application = StorePrimaryAdmissionFormDetails.objects.create(username=request.user.username,
                                                                      form_type="primary",
                                                                      email=request.user.email,
                                                                      admission_std=admission_std, dob=dob,
                                                                      student_surname=student_surname,
                                                                      student_name=student_name,
                                                                      student_father_name=student_father_name,
                                                                      student_category=student_category,
                                                                      student_caste=student_caste,
                                                                      student_gender=student_gender,
                                                                      student_religion=student_religion,
                                                                      student_blood_group=student_blood_group,
                                                                      student_present_addr=student_present_addr,
                                                                      student_telephone=student_telephone,
                                                                      student_mobile=student_mobile,
                                                                      student_previous_school=student_previous_school,
                                                                      student_previous_class=student_previous_class,
                                                                      student_previous_medium=student_previous_medium,
                                                                      student_close_landmark=student_close_landmark,
                                                                      student_known_lang=student_known_lang,
                                                                      student_allergies=student_allergies,
                                                                      student_alments=student_alments,
                                                                      student_id_mark=student_id_mark,
                                                                      student_home_time=student_home_time,
                                                                      father_surname=father_surname,
                                                                      father_name=father_name,
                                                                      father_father_name=father_father_name,
                                                                      father_age=father_age,
                                                                      father_education=father_education,
                                                                      father_work_and_addr=father_work_and_addr,
                                                                      father_designation=father_designation,
                                                                      father_income=father_income,
                                                                      father_telephone=father_telephone,
                                                                      father_mobile=father_mobile,
                                                                      mother_surname=mother_surname,
                                                                      mother_name=mother_name,
                                                                      mother_father_name=mother_father_name,
                                                                      mother_age=mother_age,
                                                                      mother_education=mother_education,
                                                                      mother_work_and_addr=mother_work_and_addr,
                                                                      mother_designation=mother_designation,
                                                                      mother_income=mother_income,
                                                                      mother_telephone=mother_telephone,
                                                                      mother_mobile=mother_mobile,
                                                                      emargency_contact=emargency_contact,
                                                                      single_parent=single_parent,
                                                                      family_type=family_type,
                                                                      family_members=family_members,
                                                                      siblings=siblings,
                                                                      sibling1_name=sibling1_name,
                                                                      sibling1_age=sibling1_age,
                                                                      sibling1_school=sibling1_school,
                                                                      sibling2_name=sibling2_name,
                                                                      sibling2_age=sibling2_age,
                                                                      sibling2_school=sibling2_school,
                                                                      bus_route_num=bus_route_num,
                                                                      bus_stop=bus_stop,
                                                                      student_photo=student_photo,
                                                                      birth_certificate=birth_certificate,
                                                                      student_adhaar_card=student_adhaar_card,
                                                                      blood_group_certificate=blood_group_certificate,
                                                                      fitness_certificate=fitness_certificate,
                                                                      parent_photo=parent_photo,
                                                                      transfer_certificate=transfer_certificate,
                                                                      report_card=report_card,
                                                                      caste_certificate=caste_certificate,
                                                                      electricity_bill=electricity_bill,
                                                                      )

        return JsonResponse({"pk":application.id})

    return render(request, 'primary_form.html')


@login_required
def pre_primary_admissions_view(request):
    # print(request.POST)
    if request.method == 'POST':
        admission_std = request.POST.get("admission_std")
        dob = request.POST.get("dob")
        student_surname = request.POST.get("student_surname")
        student_name = request.POST.get("student_name")
        student_father_name = request.POST.get("student_father_name")
        student_category = request.POST.get("student_category")
        student_caste = request.POST.get("student_caste")
        student_gender = request.POST.get("student_gender")
        student_religion = request.POST.get("student_religion")
        student_blood_group = request.POST.get("student_blood_group")
        student_present_addr = request.POST.get("student_present_addr")
        student_telephone = request.POST.get("student_telephone")
        student_mobile = request.POST.get("student_mobile")
        student_previous_school = request.POST.get("student_previous_school")
        student_previous_class = request.POST.get("student_previous_class")
        student_previous_medium = request.POST.get("student_previous_medium")
        student_close_landmark = request.POST.get("student_close_landmark")
        student_known_lang = request.POST.get("student_known_lang")
        student_allergies = request.POST.get("student_allergies")
        student_alments = request.POST.get("student_alments")
        student_id_mark = request.POST.get("student_id_mark")
        student_home_time = request.POST.get("student_home_time")

        # Family Information

        father_surname = request.POST.get("father_surname")
        father_name = request.POST.get("father_name")
        father_father_name = request.POST.get("father_father_name")
        father_age = request.POST.get("father_age")
        father_education = request.POST.get("father_education")
        father_work_and_addr = request.POST.get("father_work_and_addr")
        father_designation = request.POST.get("father_designation")
        father_income = request.POST.get("father_income")
        father_telephone = request.POST.get("father_telephone")
        father_mobile = request.POST.get("father_mobile")

        mother_surname = request.POST.get("mother_surname")
        mother_name = request.POST.get("mother_name")
        mother_father_name = request.POST.get("mother_father_name")
        mother_age = request.POST.get("mother_age")
        mother_education = request.POST.get("mother_education")
        mother_work_and_addr = request.POST.get("mother_work_and_addr")
        mother_designation = request.POST.get("mother_designation")
        mother_income = request.POST.get("mother_income")
        mother_telephone = request.POST.get("mother_telephone")
        mother_mobile = request.POST.get("mother_mobile")

        emargency_contact = request.POST.get("emargency_contact")
        single_parent = request.POST.get("single_parent")
        family_type = request.POST.get("family_type")
        family_members = request.POST.get("family_members")
        siblings = request.POST.get("siblings")
        sibling1_name = request.POST.get("sibling1_name")
        sibling1_age = request.POST.get("sibling1_age")
        sibling1_school = request.POST.get("sibling1_school")
        sibling2_name = request.POST.get("sibling2_name")
        sibling2_age = request.POST.get("sibling2_age")
        sibling2_school = request.POST.get("sibling2_school")

        bus_route_num = request.POST.get("bus_route_num")
        bus_stop = request.POST.get("bus_stop")

        # documents upload
        student_photo = request.FILES.get("student_photo")
        birth_certificate = request.FILES.get("birth_certificate")
        student_adhaar_card = request.FILES.get("student_adhaar_card")
        blood_group_certificate = request.FILES.get("blood_group_certificate")
        fitness_certificate = request.FILES.get("fitness_certificate")
        parent_photo = request.FILES.get("parent_photo")
        transfer_certificate = request.FILES.get("transfer_certificate")
        report_card = request.FILES.get("report_card")
        caste_certificate = request.FILES.get("caste_certificate")
        electricity_bill = request.FILES.get("electricity_bill")

        # print(request.POST)
        # print(request.FILES)

        application = StorePrimaryAdmissionFormDetails.objects.create(username=request.user.username,
                                                                      form_type="pre-primary",
                                                                      email=request.user.email,
                                                                      admission_std=admission_std, dob=dob,
                                                                      student_surname=student_surname,
                                                                      student_name=student_name,
                                                                      student_father_name=student_father_name,
                                                                      student_category=student_category,
                                                                      student_caste=student_caste,
                                                                      student_gender=student_gender,
                                                                      student_religion=student_religion,
                                                                      student_blood_group=student_blood_group,
                                                                      student_present_addr=student_present_addr,
                                                                      student_telephone=student_telephone,
                                                                      student_mobile=student_mobile,
                                                                      student_previous_school=student_previous_school,
                                                                      student_previous_class=student_previous_class,
                                                                      student_previous_medium=student_previous_medium,
                                                                      student_close_landmark=student_close_landmark,
                                                                      student_known_lang=student_known_lang,
                                                                      student_allergies=student_allergies,
                                                                      student_alments=student_alments,
                                                                      student_id_mark=student_id_mark,
                                                                      student_home_time=student_home_time,
                                                                      father_surname=father_surname,
                                                                      father_name=father_name,
                                                                      father_father_name=father_father_name,
                                                                      father_age=father_age,
                                                                      father_education=father_education,
                                                                      father_work_and_addr=father_work_and_addr,
                                                                      father_designation=father_designation,
                                                                      father_income=father_income,
                                                                      father_telephone=father_telephone,
                                                                      father_mobile=father_mobile,
                                                                      mother_surname=mother_surname,
                                                                      mother_name=mother_name,
                                                                      mother_father_name=mother_father_name,
                                                                      mother_age=mother_age,
                                                                      mother_education=mother_education,
                                                                      mother_work_and_addr=mother_work_and_addr,
                                                                      mother_designation=mother_designation,
                                                                      mother_income=mother_income,
                                                                      mother_telephone=mother_telephone,
                                                                      mother_mobile=mother_mobile,
                                                                      emargency_contact=emargency_contact,
                                                                      single_parent=single_parent,
                                                                      family_type=family_type,
                                                                      family_members=family_members,
                                                                      siblings=siblings,
                                                                      sibling1_name=sibling1_name,
                                                                      sibling1_age=sibling1_age,
                                                                      sibling1_school=sibling1_school,
                                                                      sibling2_name=sibling2_name,
                                                                      sibling2_age=sibling2_age,
                                                                      sibling2_school=sibling2_school,
                                                                      bus_route_num=bus_route_num,
                                                                      bus_stop=bus_stop,
                                                                      student_photo=student_photo,
                                                                      birth_certificate=birth_certificate,
                                                                      student_adhaar_card=student_adhaar_card,
                                                                      blood_group_certificate=blood_group_certificate,
                                                                      fitness_certificate=fitness_certificate,
                                                                      parent_photo=parent_photo,
                                                                      transfer_certificate=transfer_certificate,
                                                                      report_card=report_card,
                                                                      caste_certificate=caste_certificate,
                                                                      electricity_bill=electricity_bill,
                                                                      )

        # data = {"application": application}
        # pdf = render_to_pdf('../templates/pdf_template.html', data)
        return JsonResponse({"pk":application.id})

    return render(request, 'pre_primary_form.html')


@login_required
def store_admission_form_view(request):
    """
    Stores Admission application submitted by parents
    :param request: Post request contains admission form
    :return: PDF form Response
    """
    print(request.POST)
    if request.method == 'POST':
        admission_std = request.POST.get("admission_std")
        dob = request.POST.get("dob")
        student_surname = request.POST.get("student_surname")
        student_name = request.POST.get("student_name")
        student_father_name = request.POST.get("student_father_name")
        student_category = request.POST.get("student_category")
        student_caste = request.POST.get("student_caste")
        student_gender = request.POST.get("student_gender")
        student_religion = request.POST.get("student_religion")
        student_blood_group = request.POST.get("student_blood_group")
        student_present_addr = request.POST.get("student_present_addr")
        student_telephone = request.POST.get("student_telephone")
        student_mobile = request.POST.get("student_mobile")
        student_previous_school = request.POST.get("student_previous_school")
        student_previous_class = request.POST.get("student_previous_class")
        student_previous_medium = request.POST.get("student_previous_medium")
        student_close_landmark = request.POST.get("student_close_landmark")
        student_known_lang = request.POST.get("student_known_lang")
        student_allergies = request.POST.get("student_allergies")
        student_alments = request.POST.get("student_alments")
        student_id_mark = request.POST.get("student_id_mark")
        student_home_time = request.POST.get("student_home_time")

        # Family Information

        father_surname = request.POST.get("father_surname")
        father_name = request.POST.get("father_name")
        father_father_name = request.POST.get("father_father_name")
        father_age = request.POST.get("father_age")
        father_education = request.POST.get("father_education")
        father_work_and_addr = request.POST.get("father_work_and_addr")
        father_designation = request.POST.get("father_designation")
        father_income = request.POST.get("father_income")
        father_telephone = request.POST.get("father_telephone")
        father_mobile = request.POST.get("father_mobile")

        mother_surname = request.POST.get("mother_surname")
        mother_name = request.POST.get("mother_name")
        mother_father_name = request.POST.get("mother_father_name")
        mother_age = request.POST.get("mother_age")
        mother_education = request.POST.get("mother_education")
        mother_work_and_addr = request.POST.get("mother_work_and_addr")
        mother_designation = request.POST.get("mother_designation")
        mother_income = request.POST.get("mother_income")
        mother_telephone = request.POST.get("mother_telephone")
        mother_mobile = request.POST.get("mother_mobile")

        emargency_contact = request.POST.get("emargency_contact")
        single_parent = request.POST.get("single_parent")
        family_type = request.POST.get("family_type")
        family_members = request.POST.get("family_members")
        siblings = request.POST.get("siblings")
        sibling1_name = request.POST.get("sibling1_name")
        sibling1_age = request.POST.get("sibling1_age")
        sibling1_school = request.POST.get("sibling1_school")
        sibling2_name = request.POST.get("sibling2_name")
        sibling2_age = request.POST.get("sibling2_age")
        sibling2_school = request.POST.get("sibling2_school")

        bus_route_num = request.POST.get("bus_route_num")
        bus_stop = request.POST.get("bus_stop")

        # documents upload
        student_photo = request.POST.get("student_photo")
        birth_certificate = request.POST.get("birth_certificate")
        student_adhaar_card = request.POST.get("student_adhaar_card")
        blood_group_certificate = request.POST.get("blood_group_certificate")
        fitness_certificate = request.POST.get("fitness_certificate")
        parent_photo = request.POST.get("parent_photo")
        transfer_certificate = request.POST.get("transfer_certificate")
        report_card = request.POST.get("report_card")
        caste_certificate = request.POST.get("caste_certificate")
        electricity_bill = request.POST.get("electricity_bill")

        print(request)

        return HttpResponse("Form Stored Successfully!!!")

    else:
        return HttpResponseBadRequest(f"{request.method} Not Allowed")

@login_required
def applications_list_view(request):
    """
    Shows all Admission applications submitted by parents
    :param request: GET request contains admission form
    :return: Application Informations
    """
    if request.method == "GET":
        all_applications = StorePrimaryAdmissionFormDetails.objects.filter(email=request.user.email)

        print(all_applications)

        return render(request, 'applications_list.html', context={"objs": all_applications})

# @login_required
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class AdmissionApplicationView(ListView):
    def get(self, request, *args, **kwargs):
        all_applications = StorePrimaryAdmissionFormDetails.objects.filter(email=request.user.email)

        # print(all_applications)

        return render(request, 'applications_list.html', context={"objs": all_applications})


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        application = get_object_or_404(StorePrimaryAdmissionFormDetails, pk=pk)

        data = {"application": application}
        pdf = render_to_pdf('../templates/pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
