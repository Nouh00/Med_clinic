from django.urls import path
from .import views

app_name ='bills'

urlpatterns = [
    path('', views.index, name='bills'),
    path('add_bill', views.add_bill, name='add_bill'),
    path('delete_bill/<int:bill_id>', views.delete_bill, name='delete_bill'),
    path('view_bill/<int:bill_id>', views.view_bill, name='view_bill'),
]

