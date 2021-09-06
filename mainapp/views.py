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
        if form.is_valid():
            print("form is valid")
            try:
                profile1 = request.user.profile
            except Profile.DoesNotExist:
                brief_info = form.cleaned_data['brief_info']
                phone_num = form.cleaned_data['phone_num']
                twitter = form.cleaned_data['twitter']
                facebook = form.cleaned_data['facebook']
                line = form.cleaned_data['line']
                age = form.cleaned_data['age']
                home_address = form.cleaned_data['home_address']
                home_postalcode = form.cleaned_data['home_postalcode']
                home_province = form.cleaned_data['home_province']
                home_district = form.cleaned_data['home_district']
                profile1 = Profile.objects.create(user=request.user, brief_info=brief_info, phone_num=phone_num,
                 twitter=twitter, facebook=facebook, line=line, age=age, home_address=home_address, home_postalcode=home_postalcode,
                 home_district=home_district)
                print('profile does not exist so is created')
                profile1.save()
                print('profile is saved')
                messages.success(request, 'Form submission successful')
                return HttpResponseRedirect(reverse('index'))

            brief_info = form.cleaned_data['brief_info']
            phone_num = form.cleaned_data['phone_num']
            twitter = form.cleaned_data['twitter']
            facebook = form.cleaned_data['facebook']
            line = form.cleaned_data['line']
            age = form.cleaned_data['age']
            home_address = form.cleaned_data['home_address']
            home_postalcode = form.cleaned_data['home_postalcode']
            home_province = form.cleaned_data['home_province']
            home_district = form.cleaned_data['home_district']
            print(f"user is {request.user}")
            profile1 = Profile.objects.update(brief_info=brief_info, phone_num=phone_num,
                twitter=twitter, facebook=facebook, line=line, age=age, home_address=home_address, home_postalcode=home_postalcode,
                home_district=home_district)
            print('profile does exist so is created')
            print('profile is saved')
            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect(reverse('index'))
        else:
            form = ProfileForm()
            print("form is not valid")
            return render(request, 'mainapp/profile-edit.html', context={'form':form})

    # try:
    #     profile1 = request.user.profile
    #     form = ProfileForm(initial=profile1)
    #     return render(request, 'mainapp/profile-edit.html', context={'form':form})
    # except Profile.DoesNotExist:
    form = ProfileForm()
    return render(request, 'mainapp/profile-edit.html', context={'form':form})

@login_required
def username_edit(request):
    if request.method == 'POST':
        user_obj = request.user
        user_obj.first_name = str(request.POST['first_name'])
        user_obj.last_name = str(request.POST['last_name'])
        user_obj.save()
        print('user name is saved')
        messages.success(request, 'Form submission successful')
        return HttpResponseRedirect(reverse('index'))
    form = UserForm()
    return render(request, 'mainapp/username-edit.html', context={'form':form})