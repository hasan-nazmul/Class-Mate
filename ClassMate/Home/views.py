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
from rest_framework.parsers import JSONParser
import timeit

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def classroom_list(req):
    if not cache.has_key('classrooms'):
        ClassroomDBInitializer(req.user)
    return cache.get('classrooms')


def classroom_detail(req, class_id):
    if req.method == 'GET': 
        if not cache.has_key('classrooms'): 
            ClassroomDBInitializer(req.user) 
            
        classrooms = cache.get('classrooms') 
        classroom = None
        for cls in classrooms:
            if str(cls.class_id) == class_id:
                classroom = ClassroomSerializer(cls)

        return JsonResponse(classroom.data)


# Create your views here.
@login_required(login_url='/login/')
def home(req):
    if req.method == 'POST':
        data = req.POST

        class_code = data.get('class_code')
        student_name = data.get('student_name')
        student_id = data.get('student_id')

        if class_code:
            classroom = Classroom.objects.filter(class_id = class_code)[0]

            if not student_name:
                student_name = req.user.first_name
                if req.user.last_name:
                    student_name += ' ' + req.user.last_name 

            if classroom:
                enrollment = enrollment.objects.create(
                    enrolled_class = classroom,
                    student = req.user,
                    enrolled_name = student_name,
                    enrolled_id = student_id
                )
        else:
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
        
        return redirect('/home/')
    
    classrooms = classroom_list(req)

    for classroom in classrooms:
        print(classroom.cover_image)
    
    return render(req, 'homepage.html', context={'classrooms': classrooms})