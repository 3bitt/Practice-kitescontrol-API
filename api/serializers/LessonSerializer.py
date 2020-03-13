from rest_framework import serializers

from ..models import Lesson, Instructor, Student
from .StudentSerializer import StudentSerializer
from .InstructorSerializer import InstructorSerializer


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'created_date', 'student', 'instructor', 'duration', 'paid']
        read_only_fields = ['id']

    instructor = InstructorSerializer(many=True)
    student = StudentSerializer(many=True)


class CreateLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'created_date', 'student', 'instructor', 'duration', 'paid']
        read_only_fields = ['id']

    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all().order_by('-name'), many=True)
    instructor = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all(), many=True)

    def create(self, validated_data):
        student = validated_data.pop('student')
        instructor = validated_data.pop('instructor')
        lesson = Lesson.objects.create(**validated_data)
        lesson.student.set(student)
        lesson.instructor.set(instructor)
        return lesson