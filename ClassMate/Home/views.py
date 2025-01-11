from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from UserHandler.models import *
from ClassroomHandler.models import *
from .seed import *
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from ClassroomHandler.serializers import *
from django.core.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from django.contrib import messages
import timeit

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def classroom_list(req):
    classroom_keys = cache.keys('classroom:*')

    if len(classroom_keys) < req.user.classroom_count:
        ClassroomDBInitializer(req.user)
    return classroom_keys


def add_to_cash(classroom):
    cache.set(f'classroom:{classroom.class_id}', classroom)


# Create your views here.
@login_required(login_url='/login/')
def home(req):
    classroom_keys = classroom_list(req)
    classrooms = []
    for key in classroom_keys:
        classrooms.append(cache.get(key))
    return render(req, 'homepage.html', context={'classrooms': classrooms})

def createorjoinclassroom(req):
    if req.method == 'POST':
        data = req.POST

        class_code = data.get('class_code')
        student_name = data.get('student_name')
        student_id = data.get('student_id')

        if class_code:

            try: 
                classroom = Classroom.objects.filter(class_id = class_code)
                
            except (ValidationError):
                messages.warning(req, 'Invalid Code')
                return redirect('/createorjoinclassroom/')

            if not student_name:
                student_name = req.user.first_name
                if req.user.last_name:
                    student_name += ' ' + req.user.last_name

            if classroom:
                if not classroom[0].enroll_student(req.user):
                    messages.warning(req, "You've already enrolled in this class")
                else:
                    messages.success(req, "Enrollment was successful!!!")
                    req.user.classroom_count += 1
                    req.user.save()
                    add_to_cash(classroom[0])
                
                return redirect('/createorjoinclassroom/')


        else:
            class_name = data.get('class_name')
            subject = data.get('subject')
            section = data.get('section')
            description = data.get('description')

            new_classroom = Classroom.objects.create(
                instructor = req.user,
                class_name = class_name,
                subject = subject,
                section = section,
                description = description
            )

            req.user.classroom_count += 1
            req.user.save()
            add_to_cash(new_classroom)
        
        return redirect('/home/')
    return render(req, 'addjoinclass.html')