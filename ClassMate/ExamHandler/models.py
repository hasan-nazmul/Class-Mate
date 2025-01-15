from django.db import models
from UserHandler.models import *
from ClassroomHandler.models import *
import uuid
import json

class Examination(models.Model):
    exam_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='exam')
    exam_title = models.CharField(max_length=300)
    instructions = models.TextField(max_length=600)
    starting_time = models.DateTimeField()
    ending_time = models.DateTimeField()
    duration = models.DurationField()
    status = models.CharField(max_length=20, null=True, default='Upcoming')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ending_time', 'starting_time', 'duration']

    def __str__(self):
        return f'{self.exam_title}'
    

class Question(models.Model):
    question_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    order = models.IntegerField(null=True)
    question_fullmarks = models.FloatField()
    question = models.TextField(max_length=500)
    question_image = models.ImageField(upload_to='exam_question_images/')

    

class MCQ(Question):
    exam = models.ForeignKey(Examination, on_delete=models.CASCADE, related_name='mcq_questions')
    options = models.JSONField(blank=True, null=True)
    answer = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.question}'
    

class Written(Question):
    answer_sheet = models.FileField(upload_to='exam_answer_documents/')


class AnswerSheet(models.Model):
    exam = models.ForeignKey(Examination, on_delete=models.CASCADE, related_name='answer_sheet')
    submitted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='submission')
    submission_time = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    question = models.ForeignKey(MCQ, on_delete=models.CASCADE, related_name='submitted_answer')
    answer_sheet = models.ForeignKey(AnswerSheet, on_delete=models.CASCADE, related_name='answer_sheet')
    answer = models.CharField(max_length=10)