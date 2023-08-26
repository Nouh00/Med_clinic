from patients.models import secretary
from django.db import models
from prescriptions.models import Document
# Create your models here.


class Bill(Document):
    def service_default():
        return {"services": "None"}
    bill_id = models.AutoField(primary_key=True)
    total = models.IntegerField()
    note = models.TextField(null=True)
    services = models.JSONField(default=service_default)
    secretary = models.ForeignKey('patients.secretary',on_delete=models.SET_NULL, null=True, blank=True)
