from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    birth = models.DateField()
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    adresse = models.CharField(max_length=100)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    gender = models.CharField(max_length=10, null=True,choices={("F","female"),("M","male")}) 

    class Meta:
        abstract = True
    def __str__(self):
        return str(self.fname)
    

class Patient(Profile):
    patient_id = models.AutoField(primary_key=True)
    

class doctor(Profile):
    doctor_id = models.AutoField(primary_key=True)

class secretary(Profile):
    secretary_id = models.AutoField(primary_key=True)

    


