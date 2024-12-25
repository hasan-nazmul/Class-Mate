from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def test(req):
    return render(req, 'classroom.html')

def classroom(req, class_id):
    current_classroom = Teaching.objects.filter(teaching_class__class_id = class_id)[0].teaching_class
    
    if req.method == 'POST':
        image = req.FILES.get('cover_image')

        if image:
            current_classroom.cover_image = image
            current_classroom.save()

        return redirect(f'/classroom/{class_id}')

    return render(req, 'classroom.html', context={'classroom': current_classroom, 'nav': True})