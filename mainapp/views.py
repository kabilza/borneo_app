from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import BatteryRegistrationForm, ProfileForm, UserForm
from .models import Profile
from django.contrib import messages

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

@login_required
def battery_registration(request):
    if request.method == 'POST':
        updated_request = request.POST.copy()
        updated_request.update({'date_installed': request.POST['date-time']})
        form = BatteryRegistrationForm(updated_request)
        print(request.POST['date-time'])
        if form.is_valid():
            print("form is valid")
            obj = form.save(commit=False)
            try:
                profile1 = request.user.profile
            except Profile.DoesNotExist:
                profile1 = Profile.objects.create(user=request.user)
                obj.profile = profile1
                date_installed = str(request.POST['date-time'])
                print(date_installed)
                obj.date_installed = date_installed
                obj.save()
                print(request.user.profile)
                messages.success(request, 'Form submission successful')
                return HttpResponseRedirect(reverse('index'))
            obj.profile = profile1
            date_installed = str(request.POST['date-time'])
            print(date_installed)
            obj.date_installed = date_installed
            obj.save()
            print(request.user.profile)
            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect(reverse('index'))
        else:
            print("form is not valid")
            return render(request, 'mainapp/battery-register.html', context = {'form': form })
    else:
        form = BatteryRegistrationForm()
        return render(request, 'mainapp/battery-register.html', context = {'form': form })

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        form2 = UserForm(request.POST)
        if form.is_valid():
            userform = form2.save()
            print("form is valid")
            profile = form.save(commit=False)
            profile.user = userform
            profile.save()
            print('profile is saved')
            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect(reverse('index'))
        else:
            form = ProfileForm()
            form2 = UserForm()
            print("form is not valid")
            return render(request, 'mainapp/profile-edit.html', context={'form':form, 'form2':form2})

    form = ProfileForm()
    form2 = UserForm()
    return render(request, 'mainapp/profile-edit.html', context={'form':form, 'form2':form2})