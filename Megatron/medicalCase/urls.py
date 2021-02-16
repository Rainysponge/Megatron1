from django.urls import path
from . import views

urlpatterns = [
    path('case_change', views.Case, name='case_change'),
]