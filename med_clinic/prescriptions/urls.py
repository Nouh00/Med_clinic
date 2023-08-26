from django.urls import path
from .import views

app_name ='prescriptions'

urlpatterns = [
    path('', views.index, name='prescriptions'),
    path('add_prescription/', views.add_prescription, name='add_prescription'),
    path('delete_prescription/<int:presc_id>', views.delete_prescription, name='delete_prescription'),
    path('view_presc/<int:presc_id>', views.view_presc, name='view_presc')
]

