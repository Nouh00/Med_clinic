from django.shortcuts import render, redirect
from .models import Patient
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users
from appointments.forms import add_patient_form
import datetime
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.

@login_required(login_url="accounts:login")
#@allowed_users(allowed_roles=['admin','secretary','doctor'])
def index(request):
    context = {}
    url_parameter = request.GET.get("q")
    
    if url_parameter:
        patients = Patient.objects.filter(fname__icontains=url_parameter).order_by('lname')
    else:
        patients = Patient.objects.all().order_by('lname')


    if request.is_ajax():
        html = render_to_string(
            template_name="partials/patients_search.html", 
            context={"patients": patients}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)


    patient_form = add_patient_form()
    context = {
        'patients': patients,
        "patient_form":patient_form
    }
    return render(request, 'patients/index.html', context)


@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def add_patient(request):
    patient_form = add_patient_form()
    if request.method=='POST':
        patient_form = add_patient_form(request.POST)
        if patient_form.is_valid():
            patient_form.save()
            return redirect('patients:patients')

    return render(request, "patients:patients")


@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def edit_patient(request, patient_id):

    patient  = Patient.objects.get(patient_id=patient_id)
    patient_form = add_patient_form(instance=patient)

    if request.method=='POST':
        patient_form = add_patient_form(request.POST, instance=patient)
        if patient_form.is_valid():
            patient_form.save()
            return redirect('patients:patients')

    context = {"patient_form": patient_form}
    return render(request, 'patients/profile/edit_patient.html', context)



@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def delete_patient(request, patient_id):
    Patient.objects.get(patient_id=patient_id).delete()
    return redirect('patients:patients')


@login_required
def patient_profile(request, patient_id):
    patient = Patient.objects.get(patient_id=patient_id)
    td=datetime.datetime.now().date() 
    birth = patient.birth
    age = int((td-birth).days /365.25)
    patient_data = {
        'fname': patient.fname,
        'lname': patient.lname,
        'birth': patient.birth,   
        'phone': patient.phone,
        'email': patient.email,   
        'adresse': patient.adresse,
        'age': age
    }

    return render(request, 'patients/profile/patient.html', patient_data)
