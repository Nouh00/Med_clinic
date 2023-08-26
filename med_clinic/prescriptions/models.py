from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Document(models.Model):
    document_types=[(1,"prescription"),(2,"bill")]
    doc_date = models.DateTimeField(auto_now_add=True)
    doc_type = models.CharField(max_length=50, choices=document_types, null=True, blank=True)
    doctor = models.ForeignKey('patients.doctor', on_delete=models.SET_NULL, null=True, blank=True)
    patient = models.ForeignKey('patients.Patient',on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        abstract = True
    

class prescription(Document):
    def drugs_default():
        return {"drug": "None"}
        
    drug_data = models.JSONField(default=drugs_default)
    drugs_count = models.IntegerField(null=True)
    prescription_id = models.AutoField(primary_key=True)
    note = models.TextField(null=True)

    
    def __str__(self):
        return str(self.doc_type)
    