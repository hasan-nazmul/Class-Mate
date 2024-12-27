from django.shortcuts import render
from ClassroomHandler.models import *
from UserHandler.models import *
from .models import *

# Create your views here.
def examroom(req, class_id):

    current_classroom = CurrentClassroom.objects.all()[0]

    return render(req, 'examroom.html', context={'classroom': current_classroom, 'navclassroom': True, 'class_id': class_id})

def create_exam(req, class_id):
    current_classroom = CurrentClassroom.objects.all()[0]

    return render(req, 'createexam.html', context={'navclassroom': True, 'classroom': current_classroom})

def set_question(req):

    current_classroom = CurrentClassroom.objects.all()[0]

    return render(req, 'questionpaper.html', context={'navclassroom': True, 'classroom': current_classroom})