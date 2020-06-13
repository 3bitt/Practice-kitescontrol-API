from django.db.models import Exists
from rest_framework import viewsets, generics, mixins, status
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken

from .models import Student, Instructor, Lesson
from .serializers import StudentSerializer, InstructorSerializer, LessonSerializer
from rest_framework_simplejwt.tokens import RefreshToken, BlacklistMixin, OutstandingToken


# @api_view(['POST'])
# def create_auth(request):
#     serialized = UserSerializer(data=request.DATA)
#     if serialized.is_valid():
#         User.objects.create_user(
#             serialized.init_data['email'],
#             serialized.init_data['username'],
#             serialized.init_data['password']
#         )
#         return Response(serialized.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

# class getAuthTokenView(views.ObtainAuthToken):
#     serializer_class = AuthTokenSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})

# class invalidateToken(viewsets.ReadOnlyModelViewSet, BlacklistMixin):
#     serializer_class = TokenObtainSerializer
#
#     def get_queryset(self):
#         userToken = self.request.META['Authorization']
#         print(userToken)
#
#         return Response({'elo':'mordo'})


@api_view(['POST'])
def invalidateToken(request):
    try:
        requestToken = request.data['refresh']
        userToken = OutstandingToken.objects.filter(token=requestToken)
        if userToken and not BlacklistedToken.objects.filter(token__in=userToken):
            newToken = BlacklistedToken(token=userToken[0])
            newToken.save()
            return Response({'message': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'error'}, status=status.HTTP_401_UNAUTHORIZED)

    except OutstandingToken.DoesNotExist:
        return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)



# ----------  R E A D - O N L Y  ----------
#
#           LIST - RETRIEVE views
# -----------------------------------------

class InstructorReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer.InstructorSerializer

class ActiveInstructorsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Instructor.objects.filter(active = True)
    serializer_class = InstructorSerializer.InstructorSerializer


class StudentsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = Student.objects.all()
    serializer_class = StudentSerializer.StudentSerializer

    def get_queryset(self):

        orderBy = self.request.query_params.get('orderBy', None)
        queryset = Student.objects.all()

        if (orderBy == 'register_date'):
            queryset = queryset.order_by('-register_date')

        if (len(self.request.data) == 0):
            return queryset
        else:
            for query in self.request.data:
                if ( (query == 'studentName') and (len(self.request.data[query]) > 0) ):
                    queryset = queryset.filter(name__icontains=self.request.data[query], )

                elif ( (query == 'studentSurname') and (len(str(self.request.data[query])) > 0) ):
                    queryset = queryset.filter(surname__icontains=self.request.data[query] )

                elif ( (query == 'mobileNumber') and (len(self.request.data[query]) > 0) ):
                    queryset = queryset.filter(mobile_number__contains=self.request.data[query])
        return queryset

class LessonsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = Lesson.objects.all()
    serializer_class = LessonSerializer.LessonSerializer

    def get_queryset(self):

        orderBy = self.request.query_params.get('orderBy', None)
        queryset = Lesson.objects.all()

        if ( orderBy == 'date'):
            queryset = queryset.order_by('-date')

        if (len(self.request.data) == 0):
            return queryset
        else:
            for query in self.request.data:
                if ( (query == 'studentName') and (len(self.request.data[query]) > 0) ):
                    queryset = queryset.filter(student__name__icontains=self.request.data[query], )

                elif ( (query == 'studentSurname') and (len(str(self.request.data[query])) > 0) ):
                    queryset = queryset.filter(student__surname__icontains=self.request.data[query] )

                elif ( (query == 'instructorName') and (len(self.request.data[query]) > 0) ):
                    queryset = queryset.filter(instructor__name__icontains=self.request.data[query])

                elif ((query == 'instructorSurname') and (len(self.request.data[query]) > 0)):
                    queryset = queryset.filter(instructor__surname__icontains=self.request.data[query])
        return queryset


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