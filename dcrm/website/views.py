from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import error, success
# Create your views here.

def home(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            success(request, 'You have successfully logged in')
            return redirect('home')
        else:
            error(request, 'Invalid username or password')
            return render(request, 'home')
    else:   
        return render(request, 'home.html')

def login_user(request):
    pass

def logout_user(request):
    pass

