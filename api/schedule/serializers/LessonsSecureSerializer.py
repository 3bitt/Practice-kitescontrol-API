from rest_framework import serializers

from api.models import Schedule
from api.models import Student
from api.models import Lesson
from api.schedule.serializers.InstructorSecureSerializer import InstructorSecureSerializer
from api.schedule.serializers.StudentSecureSerializer import StudentSecureSerializer


class LessonsSecureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ['equipment']

    instructor = InstructorSecureSerializer(many=True)
    student = StudentSecureSerializer(many=True)
