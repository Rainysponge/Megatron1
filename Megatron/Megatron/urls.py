"""Megatron URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, diagnosis, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('diagnosis', diagnosis, name='diagnosis'),
    path('Case/', include('medicalCase.urls')),
    path('search/', search, name='search'),
    path('comment/', include('comment.urls')),
    path('user/', include('user.urls')),
    path('uploadFile/', include('fileTest.urls')),
]

urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
