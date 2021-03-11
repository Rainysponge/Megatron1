from django.urls import path, include
from . import views
# from .views import home

urlpatterns = [
    path('uploadFileInit/', views.uploadFileInit, name='uploadFile'),
    path('uploadFile_result/', views.uploadFileTest_result, name='uploadFile_result'),
    path('uploadFile_patient/', views.uploadFileTest_patient, name='uploadFile_patient'),
    path('uploadFile_illness/', views.uploadFileTest_illness, name='uploadFile_illness'),
    path('uploadFile_treatment/', views.uploadFileTest_treatment, name='uploadFile_treatment'),
    path('uploadFile_department/', views.uploadFileTest_department, name='uploadFile_department'),
    path('describe/', views.describeFunc, name='describe'),
]


