from django.db import models
from UserHandler.models import *
from ClassroomHandler.models import *
import uuid
import json


class Question(models.Model):
    question_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    order = models.IntegerField(null=True)
    question_fullmarks = models.FloatField()
    question = models.TextField(max_length=500)
    question_image = models.ImageField(upload_to='exam_question_images/')

    def to_dict(self):
        return {
            'question_id': str(self.question_id),
            'order': self.order,
            'question_fullmarks': self.question_fullmarks,
            'question': self.question,
            'question_image_url': self.question_image.url if self.question_image else None,
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())
    

class MCQ(Question):
    options = models.JSONField(blank=True, null=True)
    answer = models.CharField(max_length=10)

    def to_dict(self):
        dict = super().to_dict()
        dict['options'] = self.options
        dict['answer'] = self.answer

        return dict

    def __str__(self):
        return f'{self.question}'
    

class Written(Question):
    answer_sheet = models.FileField(upload_to='exam_answer_documents/')

    def to_dict(self):
        dict = super().to_dict()
        dict['answer_sheet_url'] = self.answer_sheet.url if self.answer_sheet else None

        return dict


# Create your models here.
class Examination(models.Model):
    exam_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='exam')
    exam_title = models.CharField(max_length=300)
    instructions = models.TextField(max_length=600)
    starting_time = models.DateTimeField()
    ending_time = models.DateTimeField()
    duration = models.DurationField()
    mcq_questions = models.ManyToManyField(MCQ, related_name='mcq_questions')
    written_questions = models.ManyToManyField(Written, related_name='written_questions')
    created_at = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            'exam_id': str(self.exam_id),
            'classroom': self.classroom.to_json(),
            'exam_title': self.exam_title,
            'instructions': self.instructions,
            'starting_time': self.starting_time.isoformat(),
            'ending_time': self.ending_time.isoformat(),
            'duration': str(self.duration),
            'mcq_questions': [str(mcq_question.id) for mcq_question in self.mcq_questions.all()],
            'written_questions': [str(written_question.id) for written_question in self.written_questions.all()],
            'created_at': self.created_at.isoformat(),
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())

    class Meta:
        ordering = ['ending_time', 'starting_time', 'duration']

    def __str__(self):
        return f'{self.exam_title}'
    