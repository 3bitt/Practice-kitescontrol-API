from rest_framework import serializers

from api.models import Schedule
from .OOO_LessonsSecureSerializer import LessonsSecureSerializer


class GenericScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = ['date', 'lessons', 'finalized']
