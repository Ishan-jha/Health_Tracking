from django import forms
from django.forms import ModelForm
from .models import User
from .models import Diagnosis


class loginForm(forms.Form):
    name = forms.CharField(label='name')
    password = forms.CharField(label='password')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'age', 'gender', 'city']

class DiagnosticsForm1(forms.Form):
    name = forms.CharField(label='name')
    doctor = forms.CharField(label='doctor')
    prescription = forms.CharField(label='prescription')
    hospital = forms.CharField(label='hospital')
    user = forms.CharField(label='user')

class DiagnosticsForm(ModelForm):
    class Meta:
        model = Diagnosis
        fields = ['name', 'doctor', 'hospital', 'prescription','patient']
