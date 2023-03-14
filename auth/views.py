from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login(request):
    form = AuthenticationForm()
    context = {'form':form}
    return render(request,'login.html',context)

def register(request):
    form = UserRegistrationForm()
    context = {'form':form}
    return render(request,'register.html',context)