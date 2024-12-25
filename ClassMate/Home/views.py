from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from UserHandler.models import *
from ClassroomHandler.models import *

# Create your views here.
@login_required(login_url='/login/')
def home(req):
    if req.method == 'POST':
        data = req.POST
        class_name = data.get('class_name')
        subject = data.get('subject')
        section = data.get('section')
        description = data.get('description')

        new_classroom = Classroom.objects.create(
            teacher = req.user,
            class_name = class_name,
            subject = subject,
            section = section,
            description = description
        )

        Teaching.objects.create(
            teaching_class = new_classroom,
            teacher = req.user
        )
        
        return redirect('/home/')

    return render(req, 'homepage.html', context={'Teaching': Teaching.objects.all()})