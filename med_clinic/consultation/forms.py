from django import forms
from .models import consultation
from patients.models import Patient



class consul_form(forms.ModelForm):
    class Meta:
        model = consultation
        fields = ('reason','examine','conclusion','patient','cons_type')
        widgets = {
            'reason':forms.Textarea(attrs={
                "class":"form-control",
                "id":"reasons-textarea",
                "rows":"5",
                "name":"reasons",
                "placeholder":"Patient Complains ..."
            }),
            'conclusion':forms.Textarea(attrs={
                "class":"form-control",
                "id":"reasons-textarea",
                "rows":"5",
                "name":"reasons",
                "placeholder":"Examination ..."
            }),
            'examine':forms.Textarea(attrs={
                "class":"form-control",
                "id":"reasons-textarea",
                "rows":"5",
                "name":"reasons",
                "placeholder":"Conclusion ..."
            }),
            'patient':forms.Select(attrs={
                "class":"form-select form-select-lg",
                "aria-label":".form-select-lg",
                "id":"patients-droplist",
                "name":"patient"
            }),
            'cons_type':forms.Select(attrs={
                "class":"form-select form-select-lg",
                "aria-label":".form-select-lg",
                "id":"emergency-droplist",
                "name":"cons_type"
            })
        }