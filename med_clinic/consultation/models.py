from django.db import models
from patients.models import Patient

# Create your models here.
class consultation(models.Model):
    cons_types = [("urgent","urgent"),("normal","normal")]
    reason = models.CharField( max_length=50)
    cons_type = models.CharField( max_length=50, choices=cons_types)
    examine =  models.CharField(max_length=50)
    conclusion = models.CharField(max_length=50)
    added_date = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey('patients.Patient',on_delete=models.SET_NULL, null=True)
    
    #def __str__(self):
    #    return self.patient