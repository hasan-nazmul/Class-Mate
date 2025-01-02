from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from UserHandler.models import *
from ClassroomHandler.models import *
from .seed import *
import json
import timeit

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

                enrolled.set(str(class_code), classroom.to_json())

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

            teaching.set(str(new_classroom.class_id), new_classroom.to_json())
        
        return redirect('/home/')

    for class_id in teaching.scan_iter():
        byte_data = teaching.get(class_id)
        json_str = byte_data.decode('utf-8')
        data_dict = json.loads(json_str)
        
        print(data_dict['class_name'])

    return HttpResponse('<h1>Home Page</h1>')