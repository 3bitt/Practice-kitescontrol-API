from django.shortcuts import render

from rest_framework import viewsets, generics, filters, mixins, request, status

from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Student, Instructor, Lesson, Schedule
from .schedule.serializers import OOO_GenericScheduleSerializer
from .serializers import StudentSerializer, InstructorSerializer, LessonSerializer, MultiSerializerViewSetMixin

from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer


class getAuthTokenView(views.ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


# ----------  R E A D - O N L Y  ----------
#
#           LIST - RETRIEVE views
# -----------------------------------------

class InstructorReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer.InstructorSerializer

class StudentsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = Student.objects.all()
    serializer_class = StudentSerializer.StudentSerializer

    def get_queryset(self):
        """ allow rest api to filter by submissions """
        queryset = Student.objects.all()

        submission = self.request.query_params.get('surname', None)
        orderBy = self.request.query_params.get('orderBy', None)
        if submission is not None:
            queryset = queryset.filter(surname=submission)
        if orderBy:
            queryset = queryset.order_by('-{}'.format(orderBy))

        return queryset

class LessonsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer.LessonSerializer


# ----------  W R I T E - O N L Y  --------
#
#               CREATE views
# -----------------------------------------

class InstructorCreateViewSet(generics.CreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer.InstructorSerializer

class StudentsCreateViewSet(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer.StudentSerializer

class LessonsCreateViewSet(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer.CreateLessonSerializer



# ------ U P D A T E --- D E S T R O Y  --------
#
#           UPDATE & DESTROY views
# -----------------------------------------

class InstructorUpdateDestroyViewSet(mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer.InstructorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        queryset = Instructor.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK )

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


class StudentUpdateDestroyViewSet(mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer.StudentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        queryset = Student.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK )
# status.HTTP_204_NO_CONTENT

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


class LessonUpdateDestroyViewSet(mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer.CreateLessonSerializer

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


class StudentSearchByQueryParams(generics.ListAPIView):
    serializer_class = StudentSerializer.StudentSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Student.objects.all()
        surname = self.request.query_params.get('surname', None)
        if surname is not None:
            queryset = queryset.filter(surname=surname)
        return queryset

class ScheduleCreateView(generics.CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = OOO_GenericScheduleSerializer.GenericScheduleSerializer