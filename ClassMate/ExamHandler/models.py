from django.db import models
from UserHandler.models import *
from ClassroomHandler.models import *
import uuid

# Create your models here.
class Examination(models.Model):
    exam_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='exam')
    exam_title = models.CharField(max_length=300)
    instructions = models.TextField(max_length=600)
    starting_time = models.DateTimeField()
    ending_time = models.DateTimeField()
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ending_time', 'starting_time', 'duration']

    def __str__(self):
        return f'{self.exam_title}'
    

class Question(models.Model):
    exam = models.ForeignKey(Examination, on_delete=models.CASCADE, related_name='question')
    question_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    order = models.IntegerField()
    question_fullmarks = models.FloatField()
    question = models.TextField(max_length=500)
    question_image = models.ImageField(upload_to='exam_images/')
    

class MCQ(Question):
    options = models.TextField(max_length=500)
    answer = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.question}'
    

class Written(Question):
    answer_sheet = models.FileField(upload_to='documents/')

