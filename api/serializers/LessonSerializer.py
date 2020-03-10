from rest_framework import serializers

from ..models import Lesson, Instructor, Student, Lesson_to_Person
from .StudentSerializer import StudentSerializer
from .InstructorSerializer import InstructorSerializer
from .LessonToPersonSerializer import LessonToPersonSerializer

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'created_date', 'student', 'instructor', 'duration', 'paid']

    # instructor = InstructorSerializer()
    instructor = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all(), many=True)
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), many=True)

    def create(self, validated_data):
        instructors = validated_data.pop('instructor')
        students = validated_data.pop('student')

        lesson = Lesson.objects.create(**validated_data)

        # lessToPerson = Lesson_to_Person.objects.create(lesson_id=lesson,
        #                                                instructor_id=)


        # for instr in instructors:
        #     for stud in students:
        #         Lesson_to_Person.objects.create(lesson_id=lesson, instructor_id=instr, student_id=stud)
        #

        for instr in instructors:
            lesson.instructor.add(instr)
            # lessToPerson.instructor_id.add(instr)
        for stud in students:
            lesson.student.add(stud)
            # lessToPerson.student_id.add(stud)
        return lesson