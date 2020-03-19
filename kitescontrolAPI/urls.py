"""kitescontrolAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api import views
from rest_framework.authtoken import views
from rest_framework_simplejwt import views as jwt_views

# router = routers.DefaultRouter()
# router.register(r'instructors', views.InstructorViewSet.as_view(), basename='instructors')
# router.register(r'students', views.StudentViewSet.as_view(), basename='students')
# router.register(r'lessons', views.LessonViewSet.as_view(), basename='lessons')

# urlpatterns = router.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    # path('api/api-token-auth/', views.ObtainAuthToken.as_view(), name='api-token-auth'),
    path('api/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair' ),
    path('api/', include('api.urls'))
    # path('', include(router.urls))
]
