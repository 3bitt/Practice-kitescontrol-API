from rest_framework import serializers

from api.models import Schedule
from .LessonsSecureSerializer import LessonsSecureSerializer


class ScheduleSecureSerializer(serializers.ModelSerializer):
    lessons = LessonsSecureSerializer(many=True)

    class Meta:
        model = Schedule
        fields = ['date', 'lessons', 'finalized']
        depth = 2



# class CustomScheduleSerializer(serializers.Serializer):
#
