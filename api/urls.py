from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from . import views
from rest_framework import routers


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# #
# router = DefaultRouter()
# router.register('lessons', views.LessonListCreateViewSet, basename='lessons')

urlpatterns = [
   re_path('lessons/$', views.LessonsReadOnlyViewSet.as_view({'get': 'list'})),
   re_path('lessons/(?P<pk>\d+)/$', views.LessonsReadOnlyViewSet.as_view({'get': 'retrieve'})),

   re_path('students/$', views.StudentsReadOnlyViewSet.as_view({'get': 'list'})),
   re_path('students/(?P<pk>\d+)/$', views.StudentsReadOnlyViewSet.as_view({'get': 'retrieve'})),
   re_path('students/create/$', views.StudentsCreateViewSet.as_view()),

   re_path('instructors/$', views.InstructorReadOnlyViewSet.as_view({'get': 'list'})),
   re_path('instructors/(?P<pk>\d+)/$', views.InstructorReadOnlyViewSet.as_view({'get': 'retrieve'})),
   re_path('instructors/create/$', views.InstructorCreateViewSet.as_view()),
   re_path('instructors/(?P<pk>\d+)/delete/$', views.InstructorUpdateDestroyViewSet.as_view({'delete':'destroy'})),
   re_path('instructors/(?P<pk>\d+)/update/$', views.InstructorUpdateDestroyViewSet.as_view({'put': 'update',
                                                                                             'patch':'partial_update'})),

   # path('lessons/', views.LessonListCreateViewSet.as_view()),
   # path('lessons/<pk>', views.LessonRetrieveUpdateDeleteViewSet.as_view()),
   # path('lessons/delete/<int:pk>', views.deleteLessonViewSet.as_view({'delete':'destroy'})),


   path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

# urlpatterns += router.urls
#

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...


