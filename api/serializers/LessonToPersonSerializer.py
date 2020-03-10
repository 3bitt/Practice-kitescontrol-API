from rest_framework import serializers

from ..models import Lesson, Instructor, Student, Lesson_to_Person


class LessonToPersonSerializer(serializers.ModelSerializer):

    lesson_id = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all())
    instructor_id = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all(), many=True, allow_null=True)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), many=True, allow_null=True)

    class Meta:
        model = Lesson_to_Person
        fields = ['lesson_id', 'instructor_id', 'student_id']

        # def create(self, validated_data):
        #     lesson = Lesson_to_Person.objects.create(**validated_data)
        #     return lesson

