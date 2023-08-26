from django.urls import path
from .import views

app_name ='drugs'

urlpatterns = [
    path('', views.index, name='drugs'),
    path('add_drug/', views.add_drug, name='add_drug'),
    path('edit_drug/<int:id>', views.edit_drug, name='edit_drug'),
    path('delete_drug/<int:id>/', views.delete_drug, name='delete_drug')
]

