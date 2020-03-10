from rest_framework import serializers

from ..models import Lesson, Instructor, Student
from .StudentSerializer import StudentSerializer
from .InstructorSerializer import InstructorSerializer


class LessonSerializer(serializers.ModelSerializer):
    # instructor = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all(), many=True)
    instructor = serializers.StringRelatedField(many=True)
    student = serializers.StringRelatedField(many=True)
    # student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all().order_by('-name'), many=True)


    # instructor = serializers.SerializerMethodField(read_only=True)
    # student = serializers.SerializerMethodField(read_only=True)
    #
    # def get_instructor(self, model):
    #     return [instructor.__str__() for instructor in model.instructor.all()]
    #
    # def get_student(self, model):
    #     return [student.__str__() for student in model.student.all().order_by('-name').distinct()]

    class Meta:
        model = Lesson
        fields = ['id', 'created_date', 'student', 'instructor', 'duration', 'paid']

    # instructor = InstructorSerializer()


    # def create(self, validated_data):
    #     instructors = validated_data.pop('instructor')
    #     students = validated_data.pop('student')
    #
    #     lesson = Lesson.objects.create(**validated_data)
    #
    #     # lessToPerson = Lesson_to_Person.objects.create(lesson_id=lesson,
    #     #                                                instructor_id=)
    #
    #
    #     # for instr in instructors:
    #     #     for stud in students:
    #     #         Lesson_to_Person.objects.create(lesson_id=lesson, instructor_id=instr, student_id=stud)
    #     #
    #
    #     for instr in instructors:
    #         lesson.instructor.add(instr)
    #         # lessToPerson.instructor_id.add(instr)
    #     for stud in students:
    #         lesson.student.add(stud)
    #         # lessToPerson.student_id.add(stud)
    #     return lesson