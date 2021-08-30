from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import BatteryRegistrationForm, ProfileForm
from .models import Profile

@login_required
def index(request):
    return render(request, 'mainapp/index.html')

def welcome(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'mainapp/welcomepage.html')

def warranty_con(request):
    return render(request, 'mainapp/warrantycondition.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'registration/signup.html', context = {'form': form })
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', context = {'form': form })

def battery_registration(request):
    if request.method == 'POST':
        form = BatteryRegistrationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            obj = form.save(commit=False)
            try:
                profile1 = request.user.profile
                obj.profile = profile1
                obj.save()
                print(request.user.profile)
                return HttpResponseRedirect(reverse('index'), {"alert": True})
            except Profile.DoesNotExist:
                profile1 = Profile.objects.create(user=request.user)
                obj.profile = profile1
                obj.save()
                print(request.user.profile)
                return HttpResponseRedirect(reverse('index'), {"alert": True})
        else:
            return render(request, 'mainapp/battery-register.html', context = {'form': form })
    else:
        form = BatteryRegistrationForm()
        return render(request, 'mainapp/battery-register.html', context = {'form': form })