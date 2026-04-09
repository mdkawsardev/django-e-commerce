from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
def index(request):
    return render(request, 'index.html')

def userLogin(request):
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        existed_user = User.objects.filter(email=email)
        if not existed_user.exists():
            add_new_user = User.objects.create(email=email, username=last_name, password=password)
            add_new_user.save()
            messages.success(request, "New user has been added successfully!")
        else:
            messages.error(request, "This user already exists!")
    return render(request, 'accounts/register.html')