from django.db.models import fields
from django.forms import widgets
import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class appoint_filter(django_filters.FilterSet):
	start_date = DateFilter(field_name="appointment_date", lookup_expr='gte')
	end_date = DateFilter(field_name="appointment_date", lookup_expr='lte')
	patient = CharFilter(field_name="patient", lookup_expr='icontains')

	class Meta:
		model = appointment
		fields = '__all__'
		exclude = ['patient','appointment_date']
		