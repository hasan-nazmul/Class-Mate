from UserHandler.models import *
from ClassroomHandler.models import *
from ExamHandler.models import *


def ClassroomDBInitializer(user):

    classrooms = Classroom.objects.filter(teacher__user_id=user.user_id)

    for classroom in classrooms:
        Teaching.objects.create(
            teaching_class = classroom,
            teacher = user
        )
        exams = Examination.objects.filter(
            classroom = classroom
        )
        for exam in exams:
            Exams.objects.create(
                exam = exam
            )

    classrooms = Enrollments.objects.filter(student__user_id=user.user_id)

    for classroom in classrooms:
        Enrolled.objects.create(
            enrolled_class = classroom
        )
        exams = Examination.objects.filter(
            classroom = classroom
        )
        for exam in exams:
            Exams.objects.create(
                exam = exam
            )