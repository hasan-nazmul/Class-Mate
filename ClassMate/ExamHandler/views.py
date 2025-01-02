# from django.shortcuts import render, redirect
# from ClassroomHandler.models import *
# from UserHandler.models import *
# from .models import *
# from datetime import datetime, timedelta

# # Create your views here.
# def examroom(req, class_id):

#     current_classroom = CurrentClassroom.objects.all()[0]

#     return render(req, 'examroom.html', context={'classroom': current_classroom, 'navclassroom': True, 'class_id': class_id})



# def create_exam(req, class_id):
#     current_classroom = CurrentClassroom.objects.all()[0]

#     if req.method == 'POST':
#         data = req.POST
#         exam_title = data.get('exam_title')
#         instructions = data.get('instructions')
#         starting_time = data.get('starting_time')
#         ending_time = data.get('ending_time')
#         duration_hours = int(data.get('duration_hours'))
#         duration_minutes = int(data.get('duration_minutes'))
#         duration_seconds = int(data.get('duration_seconds'))

#         exam = Examination.objects.create(
#             classroom = current_classroom.current_classroom,
#             exam_title = exam_title,
#             instructions = instructions,
#             starting_time = starting_time,
#             ending_time = ending_time,
#             duration = timedelta(hours=duration_hours, minutes=duration_minutes, seconds=duration_seconds)
#         )

#         exam_id = exam.exam_id

#         return redirect(f'/set-question/{class_id}/{exam_id}/')
        

#     return render(req, 'createexam.html', context={'navclassroom': True, 'classroom': current_classroom})



# def set_question(req, class_id, exam_id):

#     current_classroom = CurrentClassroom.objects.all()[0]
#     current_examination = Examination.objects.filter(
#         exam_id = exam_id
#     )[0]

#     if req.method == 'POST':
#         data = req.POST
#         question = data.get('question')
#         question_fullmarks = int(data.get('question_fullmarks'))
#         option_dict = {'options': data.getlist('option')}
#         answer = data.get('answer')
#         question_image = req.FILES.get('question_image')

#         MCQ.objects.create(
#             exam = current_examination,
#             question = question,
#             question_fullmarks = question_fullmarks,
#             question_image = question_image,
#             options = option_dict,
#             answer = answer
#         )
        
#         if data.get('add-question') == 'add_question':
#             return redirect(f'/set-question/{class_id}/{exam_id}/')

#         else:
#             return redirect(f'/examroom/{class_id}/')

#     return render(req, 'questionpaper.html', context={'navclassroom': True, 'classroom': current_classroom})