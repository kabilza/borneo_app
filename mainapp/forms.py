from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')