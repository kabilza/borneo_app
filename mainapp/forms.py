from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import Textarea
from .models import BatteryWarranty, Profile
from django import forms
 
class BatteryRegistrationForm(ModelForm):
    class Meta:
        model = BatteryWarranty
        exclude = ['profile']
        # widgets = { 'barcode': Textarea(attrs={'rows': 10})}