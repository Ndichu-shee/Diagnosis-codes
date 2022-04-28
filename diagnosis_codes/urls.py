"""diagnosis_codes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from records.views import UserViewSet,LoginUserViewSet,CsvuploadViewSet,DiagnosisCodesViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'create_user', UserViewSet, basename='create_user')
router.register(r'login_user', LoginUserViewSet, basename='login_user')
router.register(r'diagnosis-codes-upload', CsvuploadViewSet, basename="diagnosis-codes-upload")
router.register(r'diagnosis-codes', DiagnosisCodesViewSet, basename='diagnosis-codes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
 
]
