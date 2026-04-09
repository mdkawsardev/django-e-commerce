from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')

def userLogin(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')