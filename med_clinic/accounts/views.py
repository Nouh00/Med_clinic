from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .decorators import unauthenticated_user
from appointments.models import appointment
from patients.models import Patient
from prescriptions.models import prescription
from consultation.models import consultation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
import datetime

# Create your views here.

def index(request):
    login_form = AuthenticationForm()
    context = {
        "login_form":login_form,
    }
    return render(request, 'accounts/index.html',context)

@unauthenticated_user
def login_view(request):
    signup_form = UserCreationForm()
    form=AuthenticationForm()
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:    
                return redirect('appointments:appointments')
   
        
    return render(request, 'accounts/index.html', {"login_form": form, "error": "User username or password incorrect!",'signup_form':signup_form})
    


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('accounts:index')

@login_required
def dashboard(request):
    total_appointments = appointment.objects.filter(patient__isnull=False).count()
    pending_appointments = appointment.objects.filter(appointment_state='Pending', patient__isnull=False).count()
    Approved_appointments = appointment.objects.filter(appointment_state='Approved', patient__isnull=False).count()
    total_patients = Patient.objects.all().count()
    total_consult = consultation.objects.all().count()
    total_presc = prescription.objects.all().count()
    todays_appointments = appointment.objects.filter(appointment_date = datetime.date.today())
    todays_appointments = todays_appointments.filter(appointment_state='Approved', patient__isnull=False).count()

    data = {
        "pending_appointments":pending_appointments,
        "approved_appointments":Approved_appointments,
        "total_appointments":total_appointments,
        "todays_appointments": todays_appointments,
        "total_patients":total_patients,
        "total_consult":total_consult,
        "total_presc":total_presc
    }
    
    return render(request, 'accounts/status.html', data)
