from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.forms import ModelForm
from .models import BatteryWarranty, Profile
 
class BatteryRegistrationForm(ModelForm):
    class Meta:
        model = BatteryWarranty
        fields = ('username', 'password1', 'password2')