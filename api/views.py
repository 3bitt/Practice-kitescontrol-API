from django.shortcuts import render

from rest_framework import viewsets, generics, filters, mixins, request, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Student, Instructor, Lesson
from .serializers import StudentSerializer, InstructorSerializer, LessonSerializer, MultiSerializerViewSetMixin


# ---------- [R E A D - O N L Y] ----------
#
#           LIST - RETRIEVE views
# -----------------------------------------

class InstructorReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer.InstructorSerializer

class StudentsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer.StudentSerializer

class LessonsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer.LessonSerializer


# ---------- [W R I T E - O N L Y] --------
#
#               CREATE views
# -----------------------------------------

class InstructorCreateViewSet(generics.CreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer.InstructorSerializer

class StudentsCreateViewSet(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer.StudentSerializer

#TODO - Lessons create view


# ---------- [M O D I F Y - O N L Y] --------
#
#               UPDATE & DESTROY views
# -----------------------------------------

class InstructorUpdateDestroyViewSet(mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer.InstructorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # if getattr(instance, '_prefetched_objects_cache', None):
        #     # If 'prefetch_related' has been applied to a queryset, we need to
        #     # forcibly invalidate the prefetch cache on the instance.
        #     instance._prefetched_objects_cache = {}

        return Response(serializer.data)




# class LessonListCreateViewSet(generics.ListCreateAPIView):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer.LessonSerializer
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return LessonSerializer.postLessonSerializer
#         elif self.request.method == 'GET':
#             return LessonSerializer.LessonSerializer

# List and Retrieve View
class LessonListCreateViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer.LessonSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LessonSerializer.postLessonSerializer
        elif self.request.method == 'GET':
            return LessonSerializer.LessonSerializer




class LessonUpdateDeleteViewSet(mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer.LessonSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     filtered_qs = self.queryset.filter(pk='id')
    #
    #
    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return LessonSerializer.postLessonSerializer
    #     elif self.request.method == 'GET':
    #         return LessonSerializer.LessonSerializer


class deleteLessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer.LessonSerializer
    lookup_field = 'pk'


