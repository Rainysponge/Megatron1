from django.contrib import admin
from django.urls import path, include
from . import views
# from .views import home

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('docRegister/', views.docRegister, name='docRegister'),
    path('changeDocInfo/', views.changeDocInfo, name='changeDocInfo'),
    path('patientRegister/', views.patientRegister, name='patientRegister'),
]