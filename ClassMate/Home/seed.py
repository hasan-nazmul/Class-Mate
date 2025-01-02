from UserHandler.models import *
from ClassroomHandler.models import *
from ExamHandler.models import *
from django.db.models import Q
from redis import Redis
import json


teaching = Redis(host="localhost", port=6379, db=1)
enrolled = Redis(host="localhost", port=6379, db=2)


def ClassroomDBInitializer(user):
    user_classrooms = Classroom.objects.filter(
        Q(instructor=user) | Q(students=user)
    )

    for user_classroom in user_classrooms:
        if user_classroom.instructor == user:
            teaching.set(str(user_classroom.class_id), user_classroom.to_json())
        else:
            enrolled.set(str(user_classroom.class_id), user_classroom.to_json())