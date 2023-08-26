from patients.views import patient_profile
from django.shortcuts import redirect, render
from .models import prescription
from patients.models import Patient, doctor
from drugs.models import drug
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
import datetime, json
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
@login_required(login_url="accounts:login")
def index(request):
    context = {}
    url_parameter = request.GET.get("q")
    
    if url_parameter:
        presc_list = prescription.objects.filter(patient__fname__icontains=url_parameter)
    else:
        presc_list = prescription.objects.all()


    if request.is_ajax():
        html = render_to_string(
            template_name="partials/prescriptions_search.html", 
            context={"presc_list": presc_list}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    user = request.user.groups.get()
    patients_list = Patient.objects.all()
    doctors_list = doctor.objects.all()
    drugs_list = drug.objects.all()
    context = {
        "presc_list":presc_list,
        "patients_list":patients_list,
        "doctors_list":doctors_list,
        "drugs_list":drugs_list,
        "user":str(user)
    }
    return render(request, "prescriptions/index.html", context)



@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','doctor'])
def add_prescription(request):
    drugs= {}
    if request.method == 'POST':
        x = 1
        while x <= int(request.POST['drugs_count']):
            drugs[x]= {}
            for k,v in request.POST.items():
                if str(k).endswith(str(x)):
                    drugs[x][k] = v
            x += 1        
        
        
        doc = doctor.objects.get(doctor_id=request.POST['doctor'])
        patient = Patient.objects.get(patient_id=request.POST['patient'])
        add_presc = prescription.objects.create(
            doctor=doc,
            patient=patient,
            note=request.POST['note'],
            doc_type="prescription",
            drug_data = drugs,
            )
        print(drugs)
        print(int(request.POST['drugs_count']))
        return redirect('prescriptions:prescriptions')


@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','doctor'])    
def delete_prescription(request, presc_id):
    prescriptions = prescription.objects.get(prescription_id=presc_id).delete()
    return redirect("prescriptions:prescriptions")


@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def view_presc(request, presc_id):
    prescriptions =prescription.objects.get(prescription_id=presc_id)
    birth = prescriptions.patient.birth
    td=datetime.datetime.now().date() 
    age = int((td-birth).days /365.25)
    patient_data = {
        'fname': prescriptions.patient.fname,
        'lname': prescriptions.patient.lname,
        'birth': prescriptions.patient.birth,   
        'phone': prescriptions.patient.phone,
        'email': prescriptions.patient.email,   
        'adresse': prescriptions.patient.adresse,
        'age': age
    }

    context={
        "drug_data": prescriptions.drug_data,
        "presc_data": prescriptions,
        "patient":patient_data
    }
    return render(request, "prescriptions/prescription-view.html", context)
        

