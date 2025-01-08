from UserHandler.models import *
from ClassroomHandler.models import *
from ExamHandler.models import *
from django.db.models import Q
from redis import Redis
from rest_framework.renderers import JSONRenderer
from ClassroomHandler.serializers import *
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def ClassroomDBInitializer(user):
    classroom_queryset = Classroom.objects.filter(
        Q(instructor=user) | Q(students=user)
    )
    cache.set('classrooms', classroom_queryset)