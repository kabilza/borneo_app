from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    message = 'Welcome to index!'
    return render(request, 'mainapp/indexpage.html')
