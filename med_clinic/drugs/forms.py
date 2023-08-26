from django import forms
from django.db import models
from django.forms import widgets
from .models import drug


class add_drug_form(forms.ModelForm):
    required = True
    drug_category=[(1,"Lequid"),(2,"Pill"),(3,"Vaccine")]
    class Meta:
        model = drug
        fields = ("brand","name","category")
        widgets={
            'name': forms.TextInput(attrs={
                "class":"form-control form-control-lg",
                "placeholder": "Drug name ..",
                "id":"colFormLabelLg",
            }),
            'brand': forms.TextInput(attrs={
                "class":"form-control form-control-lg",
                "placeholder": "Drug brand .."
            }),
            'category': forms.Select(attrs={
                "class":"form-select form-select-lg",
                "aria-label":".form-select-lg",
                "placeholder": "Drug Category ..",
                "id":"drugscategory-droplist"
            },
            choices=[("Lequid","lequid"),("Pill","pill"),("Vaccine","vaccine")]
            )}