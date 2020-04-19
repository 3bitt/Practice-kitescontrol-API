from django.db.models import Q
from rest_framework import serializers

from api.models import Schedule, Instructor, Lesson
from .InstructorSecureSerializer import InstructorSecureSerializer
from .LessonScheduleSerializer import LessonsScheduleSerializer
from .LessonsSecureSerializer import LessonsSecureSerializer
from ...serializers.InstructorSerializer import InstructorSerializer
from ...serializers.LessonSerializer import LessonSerializer


class ScheduleSecureSerializer(serializers.ModelSerializer):
    lessons = LessonsSecureSerializer(many=True)

    class Meta:
        model = Schedule
        fields = ['date', 'lessons', 'finalized']
        depth = 2




class CustomInstrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        exclude = ['birth_date',
                   'mobile_number',
                   'weight',
                   'available_from',
                   'available_to',
                   'pay_rate',
                   'english_lessons',
                   'kids_lessons',
                   'group_lessons',
                   'daily_hour_limit',
                   'active']

    lessons = LessonsScheduleSerializer(many=True, read_only=True)


class CustomScheduleSerializer(serializers.Serializer):

    # date = serializers.DateField(read_only=True)
    # instructors = CustomInstrSerializer(many=True, read_only=True)
    instructors = CustomInstrSerializer(many=True)

