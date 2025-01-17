from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from api.schedule.views.scheduleView import api_custom_schedule_view
from api.statistics.views.instructorHoursView import api_get_instructor_hours
from rest_framework_simplejwt import views as jwt_views

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

urlpatterns = [

   path('authenticateUser/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('refreshToken/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
   path('verifyToken/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
   path('logout/', views.invalidateToken),

   re_path('instructors/hours', api_get_instructor_hours, name='instructor hours'),
   re_path('custom', api_custom_schedule_view, name='custom'),

   re_path('lessons/$', views.LessonsReadOnlyViewSet.as_view({'get': 'list',
                                                              'post':'list'})),
   re_path('lessons/(?P<pk>\d+)/$', views.LessonsReadOnlyViewSet), #.as_view({'get': 'retrieve'})
   re_path('lessons/create/$', views.LessonsCreateViewSet.as_view()),
   re_path('lessons/(?P<pk>\d+)/delete/$', views.LessonUpdateDestroyViewSet.as_view({'delete': 'destroy'})),
   re_path('lessons/(?P<pk>\d+)/update/$', views.LessonUpdateDestroyViewSet.as_view({'put': 'update',
                                                                                     'patch': 'partial_update'})),
   # re_path('students/<str:surname>', views.StudentSearchByQueryParams.as_view()),
   re_path('students/$', views.StudentsReadOnlyViewSet.as_view({'get': 'list',
                                                                'post': 'list'})),
   re_path('students/(?P<pk>\d+)/$', views.StudentsReadOnlyViewSet.as_view({'get': 'retrieve'})),
   re_path('students/create/$', views.StudentsCreateViewSet.as_view()),
   re_path('students/(?P<pk>\d+)/delete/$', views.StudentUpdateDestroyViewSet.as_view({'delete': 'destroy'})),
   re_path('students/(?P<pk>\d+)/update/$', views.StudentUpdateDestroyViewSet.as_view({'put': 'update',
                                                                                       'patch': 'partial_update'})),


   re_path('instructors/$', views.InstructorReadOnlyViewSet.as_view({'get': 'list'})),
   re_path('activeInstructors/$', views.ActiveInstructorsViewSet.as_view({'get':'list'})),
   re_path('instructors/(?P<pk>\d+)/$', views.InstructorReadOnlyViewSet.as_view({'get': 'retrieve'})),
   re_path('instructors/create/$', views.InstructorCreateViewSet.as_view()),
   re_path('instructors/(?P<pk>\d+)/delete/$', views.InstructorUpdateDestroyViewSet.as_view({'delete':'destroy'})),
   re_path('instructors/(?P<pk>\d+)/update/$', views.InstructorUpdateDestroyViewSet.as_view({'put': 'update',
                                                                                             'patch':'partial_update'})),
   # path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   # path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

# silk - DRF debugger
urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
