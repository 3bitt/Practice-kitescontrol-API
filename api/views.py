from django.shortcuts import render

from rest_framework import viewsets, generics, filters, mixins, request
from rest_framework.decorators import action
from .models import Student, Instructor, Lesson
from .serializers import StudentSerializer, InstructorSerializer, getLessonSerializer, MultiSerializerViewSetMixin



# ------------------ # ------------------
#####       LIST - CREATE views
# ------------------ # ------------------


class StudentsListCreateViewSet(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer.StudentSerializer


class InstructorListCreateViewSet(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer.InstructorSerializer

class LessonListCreateViewSet(MultiSerializerViewSetMixin.MultiSerializerViewSetMixin, generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = getLessonSerializer.getLessonSerializer
    serializer_action_classes = {
        'list': getLessonSerializer.getLessonSerializer,
        'post': getLessonSerializer.postLessonSerializer
    }
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return getLessonSerializer.postLessonSerializer
        elif self.request.method == 'GET':
            return getLessonSerializer.getLessonSerializer


class deleteLessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = getLessonSerializer.getLessonSerializer
    lookup_field = 'pk'


