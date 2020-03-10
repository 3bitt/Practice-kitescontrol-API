from django.conf.urls import url
from django.urls import path, include
from . import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'instructors', views.getInstructorViewSet, basename='instructors')
# router.register(r'students', views.getStudentViewSet, basename='students')
# router.register(r'lessons', views.getLessonViewSet, basename='lessons')

# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = [
    path('students/', views.StudentsListCreateViewSet.as_view()),
    path('instructors/', views.InstructorListCreateViewSet.as_view()),
    path('lessons/', views.LessonListCreateViewSet.as_view()),
    path('delete/<int:pk>', views.deleteLessonViewSet.as_view({'delete':'destroy'}))
    # path('api/^', router.urls)
]



