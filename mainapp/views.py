from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'mainapp/index.html')

def welcome(request):
    return render(request, 'mainapp/welcomepage.html')

def warranty_con(request):
    return render(request, 'mainapp/warrantycondition.html')