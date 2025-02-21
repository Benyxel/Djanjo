from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *
# Create your views here.

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        user_data_has_error = False
        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, "Username already exists")
            
        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, "Email already exists")
            
        if len(password1) < 8:
            user_data_has_error = True
            messages.error(request, "Password must be at least 8 characters")
        
        if password1 != password2:
            user_data_has_error = True
            messages.error(request, "Passwords do not match")
        
        if user_data_has_error:
            return redirect('register')
        
        else:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password1
            )
            
            messages.success(request, "Account created successfully. Login now")
            return redirect('login')
        
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')



