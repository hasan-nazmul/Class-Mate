from rest_framework import serializers
from .models import Examination, MCQ, Written, Question
from ClassroomHandler.models import *

class ExaminationSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all())
    mcq_questions = serializers.PrimaryKeyRelatedField(many=True, queryset=MCQ.objects.all())
    written_questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Written.objects.all())

    class Meta:
        model = Examination
        fields = [
            'exam_id',
            'classroom',
            'exam_title',
            'instructions',
            'starting_time',
            'ending_time',
            'duration',
            'mcq_questions',
            'written_questions',
            'created_at'
        ]

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'question_id',
            'order',
            'question_fullmarks',
            'question',
            'question_image'
        ]

class MCQSerializer(QuestionSerializer):
    class Meta(QuestionSerializer.Meta):
        model = MCQ
        fields = QuestionSerializer.Meta.fields + [
            'options',
            'answer'
        ]

class WrittenSerializer(QuestionSerializer):
    class Meta(QuestionSerializer.Meta):
        model = Written
        fields = QuestionSerializer.Meta.fields + [
            'answer_sheet'
        ]
