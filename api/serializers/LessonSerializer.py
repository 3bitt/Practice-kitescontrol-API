from rest_framework import serializers

from ..models import Lesson, Instructor, Student
from .StudentSerializer import StudentSerializer
from .InstructorSerializer import InstructorSerializer


class LessonSerializer(serializers.ModelSerializer):

    # instructor = serializers.StringRelatedField(many=True)
    # student = serializers.StringRelatedField(many=True)
    instructor = InstructorSerializer(many=True)
    student = StudentSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ['id', 'created_date', 'student', 'instructor', 'duration', 'paid']

    # def create(self, validated_data):
    #


class postLessonSerializer(serializers.ModelSerializer):

    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all().order_by('-name'), many=True)
    instructor = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all(), many=True)
    class Meta:
        model = Lesson
        fields = ['id', 'created_date', 'student', 'instructor', 'duration', 'paid']


        # instructor = serializers.SerializerMethodField(read_only=True)
        # student = serializers.SerializerMethodField(read_only=True)
        #
        # def get_instructor(self, model):
        #     return [instructor.__str__() for instructor in model.instructor.all()]
        #
        # def get_student(self, model):
        #     return [student.__str__() for student in model.student.all().order_by('-name').distinct()]