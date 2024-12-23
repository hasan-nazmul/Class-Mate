from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from UserHandler.models import *

# Create your views here.
@login_required(login_url='/login/')
def home(req):
    return render(req, 'homepage.html')