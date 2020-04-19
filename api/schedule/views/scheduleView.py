from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Lesson, Schedule, Instructor
from api.schedule.serializers.ScheduleSecureSerializer import ScheduleSecureSerializer, CustomScheduleSerializer
from api.serializers.LessonSerializer import LessonSerializer

@api_view(['GET'])
def api_detail_schedule_view(request, pk):

    try:
        schedule = Schedule.objects.get(pk=pk)
    except Schedule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = ScheduleSecureSerializer(schedule)
        return Response(serializer.data)

@api_view(['GET'])
def api_custom_schedule_view(request):

    try:
        date = request.query_params.get('date', None)

        ins = Instructor.objects.raw(
            ''' select * from api_instructor
                where id in (
                    select instructor_id from api_lesson_instructor
                    where lesson_id in(
                        select id from api_lesson
                        where date=%s
                        )
                    )''', [date]
        )

        instructors = Instructor.objects.filter(lessons__in= Lesson.objects.filter(date=date)).distinct()

        res = {'instructors': []}
        for inst in instructors:
            res['instructors'].append(inst)

        serializer = CustomScheduleSerializer(res)


        return Response(serializer.data)

    except Lesson.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
