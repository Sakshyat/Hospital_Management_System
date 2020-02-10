from django import forms
from .models import Patient, Appointment, Report

class AppForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('appointment_date', 'appointment_time')
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('appointment_date', 'appointment_time')
        
class RepForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('rep_type', 'pdf')