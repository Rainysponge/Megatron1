from django.urls import path
from . import views

urlpatterns = [
    # http://http://127.0.0.1:8000/Apprenticeship/
    path('find_result/', views.find_result, name='find_result'),
]
