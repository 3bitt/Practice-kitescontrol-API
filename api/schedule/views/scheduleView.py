from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Lesson, Instructor
from api.schedule.serializers.abcSerializer import abcSerializer
from api.serializers.LessonSerializer import LessonSerializer

@api_view(['GET'])
def api_custom_schedule_view(request):

    try:
        query_date = request.query_params.get('date', None)
        lessons = Lesson.objects.filter(date=query_date).order_by('time')
        serializer = abcSerializer(lessons)
        return Response(serializer.data)
    except Lesson.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
