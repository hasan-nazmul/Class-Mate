from UserHandler.models import *
from ClassroomHandler.models import *


def TeachingDBInitializer(user):
    classrooms = Classroom.objects.filter(teacher__user_id=user.user_id)

    for classroom in classrooms:
        Teaching.objects.create(
            teaching_class = classroom,
            teacher = user
        )