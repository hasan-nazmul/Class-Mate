from django.shortcuts import render, redirect
from .models import *
from ClassroomHandler.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from Home.seed import *

# Create your views here.
def landing_page(req):
    return render(req, 'landing.html')

def login_page(req):
    if req.user.is_authenticated:
        return redirect('/home/')
    
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = CustomUser.objects.filter(username=username)

        if not user.exists():
            messages.info(req, "Invalid username!")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(req, "Wrong Password!")
            return redirect('/login/')
        
        else:
            login(req, user)
            TeachingDBInitializer(user)
            return redirect('/home/')

    return render(req, 'login.html')

def signup_page(req):
    if req.user.is_authenticated:
        return redirect('/home/')
    
    if req.method == 'POST':
        data = req.POST
        username = data.get('username')
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        user = CustomUser.objects.filter(username=username)

        if user.exists():
            messages.info(req, "Username already taken!")
            return redirect('/signup/')
        
        user = CustomUser.objects.filter(email=email)

        if user.exists():
            messages.info(req, "Email already taken!")
            return redirect('/signup/')
        
        if password != confirm_password:
            messages.info(req, "Passwords didn't match!")
            return redirect('/signup/')

        user = CustomUser.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email
        )

        user.set_password(password)

        user.save()

        messages.error(req, "Account created successfully!")

        return redirect('/login/')

    return render(req, 'signup.html')

def logout_page(req):
    logout(req)
    Teaching.objects.all().delete()
    return redirect('/')