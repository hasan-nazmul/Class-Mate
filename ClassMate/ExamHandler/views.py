from django.shortcuts import render, redirect
from ClassroomHandler.models import *
from UserHandler.models import *
from .models import *
from datetime import datetime, timedelta
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# Create your views here.
def examroom(req, class_id):
    current_classroom = cache.get(f'classroom:{class_id}')

    if not current_classroom:
        current_classroom = Classroom.objects.filter(class_id = class_id)[0]
        cache.set(f'classroom:{class_id}', current_classroom)

    exams = []

    for exam in current_classroom.exam.all():
        if not cache.has_key(f'exam:{exam.exam_id}'):
            examination = Examination.objects.filter(exam_id=exam.exam_id)[0]
            cache.set(f'exam:{exam.exam_id}', examination)
        
        exams.append(cache.get(f'exam:{exam.exam_id}'))

    return render(req, 'examroom.html', context={'classroom': current_classroom, 'exams': exams})


def create_exam(req, class_id):
    current_classroom = cache.get(f'classroom:{class_id}')

    if not current_classroom:
        current_classroom = Classroom.objects.filter(class_id = class_id)[0]
        cache.set(f'classroom:{class_id}', current_classroom)

    if req.method == 'POST':
        data = req.POST
        exam_title = data.get('exam_title')
        instructions = data.get('instructions')
        starting_time = data.get('starting_time')
        ending_time = data.get('ending_time')
        duration_hours = int(data.get('duration_hours'))
        duration_minutes = int(data.get('duration_minutes'))
        duration_seconds = int(data.get('duration_seconds'))

        exam = Examination.objects.create(
            classroom = current_classroom,
            exam_title = exam_title,
            instructions = instructions,
            starting_time = starting_time,
            ending_time = ending_time,
            duration = timedelta(hours=duration_hours, minutes=duration_minutes, seconds=duration_seconds)
        )

        cache.set(f'exam:{exam.exam_id}', exam)

        exam_id = exam.exam_id

        return redirect(f'/set-question/{class_id}/{exam_id}/')
        

    return render(req, 'createexam.html', context={'classroom': current_classroom})



def set_question(req, class_id, exam_id):

    current_classroom = cache.get(f'classroom:{class_id}')

    if not current_classroom:
        current_classroom = Classroom.objects.filter(class_id = class_id)[0]
        cache.set(f'classroom:{class_id}', current_classroom)

    current_examination = cache.get(f'exam:{exam_id}')

    if not current_examination:
        current_examination = Examination.objects.filter(
            exam_id = exam_id
        )[0]
        cache.set(f'exam:{current_examination.exam_id}', current_examination)

    if req.method == 'POST':
        data = req.POST
        question = data.get('question')
        question_fullmarks = int(data.get('question_fullmarks'))
        option_dict = {'options': data.getlist('option')}
        answer = data.get('answer')
        question_image = req.FILES.get('question_image')

        mcq = MCQ.objects.create(
            exam = current_examination,
            question=question,
            question_fullmarks = question_fullmarks,
            question_image = question_image,
            options = option_dict,
            answer = answer,
        )

        if data.get('submit'):
            return redirect(f'/examroom/{class_id}')
        

    return render(req, 'questionpaper.html', context={'classroom': current_classroom})


def submission(req, exam_id):
    pass
