from django.shortcuts import redirect, render
from .models import Bill
from patients.models import Patient,doctor,secretary
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.
def index(request):
    context = {}
    url_parameter = request.GET.get("q")
    
    if url_parameter:
        bills_list = Bill.objects.filter(patient__fname__icontains=url_parameter)
    else:
        bills_list = Bill.objects.all()
    if request.is_ajax():
        html = render_to_string(
            template_name="partials/bills_search.html", 
            context={"bills_list": bills_list}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    
    patients_list = Patient.objects.all()
    doctors_list = doctor.objects.all()
    secretaries_list = secretary.objects.all()
    context = {
        "bills_list":bills_list,
        "patients_list":patients_list,
        "doctors_list":doctors_list,
        "secretaries_list": secretaries_list
    }
    return render(request, "bills/index.html", context)


def add_bill(request):
    services = {}
    if request.method == 'POST':
        x = 1
        while x <= int(request.POST['services_count']):
            services[x] = {}
            for k,v in request.POST.items():
                if str(k).endswith(str(x)):
                     services[x][k] = v
            x += 1

        doct = doctor.objects.get(doctor_id=request.POST['doctor1'])
        patient = Patient.objects.get(patient_id=request.POST['patient1'])
        secr = secretary.objects.get(secretary_id=request.POST['secretary1'])
        add_bill = Bill.objects.create(
            doc_type = "bill",
            doctor = doct,
            patient = patient,
            secretary = secr,
            total = int(request.POST['total']),
            note = request.POST['note'],
            services = services
        )
        print(services)
        print(int(request.POST['services_count']))
        return redirect('bills:bills')


def delete_bill(request, bill_id):
    bills = Bill.objects.get(bill_id=bill_id).delete()
    return redirect("bills:bills")    
        

def view_bill(request, bill_id):
    bills = Bill.objects.get(bill_id=bill_id)
    patient_data = {
        'fname': bills.patient.fname,
        'lname': bills.patient.lname,  
        'phone': bills.patient.phone,
        'email': bills.patient.email,   
        'adresse': bills.patient.adresse,
    }

    context={
        "bill_data": bills,
        "patient_data":patient_data,
        "services":bills.services
    }
    return render(request, "bills/bill-view.html", context)