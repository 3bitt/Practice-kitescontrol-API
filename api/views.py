from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.decorators import action
from .models import Student, Instructor, Lesson, Lesson_to_Person
from .serializers import StudentSerializer, InstructorSerializer, LessonSerializer
from .serializers.LessonToPersonSerializer import LessonToPersonSerializer



# ------------------ # ------------------
#####       LIST - CREATE views
# ------------------ # ------------------


class getStudentViewSet(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer.StudentSerializer

class getInstructorViewSet(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer.InstructorSerializer

class getLessonViewSet(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer.LessonSerializer

class deleteLessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer.LessonSerializer
    lookup_field = 'pk'


