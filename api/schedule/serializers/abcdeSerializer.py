from django.db.models import Q
from rest_framework import serializers

from .LessonScheduleSerializer import LessonsScheduleSerializer


class abcdeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    surname = serializers.CharField(max_length=30)
    weight = serializers.FloatField()

    lessons = serializers.SerializerMethodField('get_lessons')

    def get_lessons(self, instr):
        querySet = self.context.get('lessons')
        lessons = querySet.filter(instructor=instr)
        serializer = LessonsScheduleSerializer(lessons, many=True)
        return serializer.data

