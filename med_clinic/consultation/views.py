from patients.models import Patient
from django.shortcuts import redirect, render
from .forms import consul_form
from .models import consultation
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
import datetime
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.
@login_required(login_url="accounts:login")
def index(request):
    context = {}
    url_parameter = request.GET.get("q")
    
    if url_parameter:
        consultations = consultation.objects.filter(patient__fname__icontains=url_parameter)
    else:
        consultations = consultation.objects.all()

    

    if request.is_ajax():
        html = render_to_string(
            template_name="partials/consultations_search.html", 
            context={"consultations": consultations}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)
    user = request.user.groups.get()
    consult_form = consul_form()
    patients = Patient.objects.all()
    context = {
        "consult_form":consult_form,
        "consultations":consultations,
        "patients":patients,
        "user":str(user)
    }
    return render(request, "consultation/index.html", context)

@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','doctor'])
def add_consult(request):
    consult_form = consul_form()
    if request.method=='POST':
        consult_form = consul_form(request.POST)
        if consult_form.is_valid():
            consult_form.save()
            print("saved!")
        return redirect("consultations:consultations")
    
    print("not yet!")
    return render(request, "consultations:consultations")

@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def view_consult(request, consult_id):
    consultations = consultation.objects.get(id=consult_id)
    birth = consultations.patient.birth
    td=datetime.datetime.now().date() 
    age = int((td-birth).days /365.25)
    patient_data = {
        'fname': consultations.patient.fname,
        'lname': consultations.patient.lname,
        'birth': consultations.patient.birth,   
        'phone': consultations.patient.phone,
        'email': consultations.patient.email,   
        'adresse': consultations.patient.adresse,
        'age': age
    }

    context={
        "consultation_data":consultations,
        "patient":patient_data
    }

    return render(request, "consultation/consultation-view.html", context)

def delete_consult(request, consult_id):
    consultations = consultation.objects.get(id=consult_id).delete()
    return redirect("consultations:consultations")   