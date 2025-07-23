from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import Newuser
from django.contrib.auth.hashers import make_password
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
# Create your views here.
def register_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        
        # validating our information ie email and password
        user_data_has_error = False
        
        if Newuser.objects.filter(username=username).exists():
            user_data_has_error = True
            # creating an error message
            messages.error(request, "Username already exists")
        
        if Newuser.objects.filter(email=email).exists():
            user_data_has_error = True
            # creating the error message
            messages.error(request, "Account with this email already exists")
        # working on the length of a password
        if len(password) < 8:
            user_data_has_error = True
            messages.error(request, "Password must be atleast 8 characters")
        # validating the password
        if confirm_password != password:
            user_data_has_error = True
            messages.error(request, "Password does not match")
        
        # if datahas errors,, what should be done
        if user_data_has_error:
            return redirect('register')
        # else what
        else:
            Newuser.objects.create(username=username,email=email,contact=contact,password=make_password(password))
            messages.success(request, "User created successfully")
            return redirect('login')
    return render(request, 'registration/register.html')
# login view
def login_user(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # authentication
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('sowaf:home')
        else:
            messages.error(request, "Invalid credentials given")
    return render(request, 'registration/login.html')