from django.db.models import Q
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from api.models import Schedule, Instructor, Lesson
from .InstructorSecureSerializer import InstructorSecureSerializer
from .LessonScheduleSerializer import LessonsScheduleSerializer
from .OOO_LessonsSecureSerializer import LessonsSecureSerializer
from ...serializers.InstructorSerializer import InstructorSerializer
from ...serializers.LessonSerializer import LessonSerializer


class ScheduleSecureSerializer(serializers.ModelSerializer):
    lessons = LessonsSecureSerializer(many=True)

    class Meta:
        model = Schedule
        fields = ['date', 'lessons', 'finalized']
        depth = 2

class CustomInstrSerializer(serializers.Serializer):
    # lessons = SerializerMethodField('get_lessons')

    # class Meta:
    #     model = Instructor
    #     exclude = ['birth_date',
    #                'mobile_number',
    #                'weight',
    #                'available_from',
    #                'available_to',
    #                'pay_rate',
    #                'english_lessons',
    #                'kids_lessons',
    #                'group_lessons',
    #                'daily_hour_limit',
    #                'active']

    # def get_lessons(self, instr):
    #     les = Lesson.objects.filter(instructor=instr).order_by('time')
    #     serializer = LessonsScheduleSerializer(instance=les, many=True)
    #     return serializer.data
    instructor = serializers.SerializerMethodField('get_instructor')
    lessons = serializers.SerializerMethodField('get_lessons')
    # lessons = LessonsScheduleSerializer(many=True, read_only=True)

    def get_instructor(self, instr):
        i = Instructor.objects.get(pk=instr.id)
        serializer = InstructorSecureSerializer(i)
        return serializer.data

    def get_lessons(self, instr):
        querySet = self.context.get('lessons')
        lessons = querySet.filter(instructor=instr)
        serializer = LessonsScheduleSerializer(lessons, many=True)
        return serializer.data

class CustomScheduleSerializer(serializers.Serializer):

    # date = serializers.DateField(read_only=True)
    # instructors = CustomInstrSerializer(many=True, read_only=True)
    instructors = CustomInstrSerializer(many=True)

