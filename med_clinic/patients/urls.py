from django.urls import path
from .import views


app_name = 'patients'

urlpatterns = [
    path('', views.index, name='patients'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('edit_patient/<int:patient_id>/', views.edit_patient, name='edit_patient'),
    path('patient_profile/<int:patient_id>/', views.patient_profile, name='patient_profile'),
    path('delete_patient/<int:patient_id>/', views.delete_patient, name='delete_patient')
]
