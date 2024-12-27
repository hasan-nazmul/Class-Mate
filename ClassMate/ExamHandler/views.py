from django.shortcuts import render
from ClassroomHandler.models import *
from UserHandler.models import *
from .models import *

# Create your views here.
def examroom(req, class_id):

    current_classroom = Teaching.objects.filter(teaching_class__class_id = class_id)

    if not current_classroom:
        current_classroom = Enrolled.objects.filter(enrolled_class__enrolled_class__class_id = class_id)[0].enrolled_class.enrolled_class

    else:
        current_classroom = current_classroom[0].teaching_class

    return render(req, 'questionpaper.html', context={'classroom': current_classroom, 'navclassroom': True})