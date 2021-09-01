from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import Textarea
from .models import BatteryWarranty, Profile

class BatteryRegistrationForm(ModelForm):
    class Meta:
        model = BatteryWarranty
        exclude = ['profile']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']