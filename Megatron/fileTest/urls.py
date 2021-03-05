from django.urls import path, include
from . import views
# from .views import home

urlpatterns = [
    path('uploadFile/', views.uploadFileTest, name='uploadFile'),
]