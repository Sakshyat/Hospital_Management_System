from django import forms
from django.contrib.auth.models import User
from patient.models import Patient
from doctor.models import Doctor


class RegForm(forms.ModelForm):
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
 #start   
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('address','contact')
    
class DashForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('doc_id','doc_name','doc_email','specialisation','qualification','image')
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('doc_name','doc_email','specialisation','qualification')
        
        