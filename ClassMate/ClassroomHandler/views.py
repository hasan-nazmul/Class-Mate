from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def test(req):
    return render(req, 'classroom.html')

def classroom(req, class_id):
    current_classroom = Teaching.objects.filter(teaching_class__class_id = class_id)

    if not current_classroom:
        current_classroom = Enrolled.objects.filter(enrolled_class__enrolled_class__class_id = class_id)[0].enrolled_class.enrolled_class

    else:
        current_classroom = current_classroom[0].teaching_class
    
    if req.method == 'POST':
        image = req.FILES.get('cover_image')

        if image:
            current_classroom.cover_image = image
            current_classroom.save()

        return redirect(f'/classroom/{class_id}')

    return render(req, 'classroom.html', context={'classroom': current_classroom, 'navclassroom': True})

def peoples(req, class_id):
    current_classroom = Teaching.objects.filter(teaching_class__class_id = class_id)

    if not current_classroom:
        current_classroom = Enrolled.objects.filter(enrolled_class__enrolled_class__class_id = class_id)[0].enrolled_class.enrolled_class

    else:
        current_classroom = current_classroom[0].teaching_class

    teacher = current_classroom.teacher

    students = Enrollments.objects.filter(
        enrolled_class = current_classroom
    )

    return render(req, 'peoples.html', context={'classroom': current_classroom, 'teacher': teacher, 'students': students, 'navclassroom': True})