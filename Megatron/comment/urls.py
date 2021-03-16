from django.urls import path
from . import views

urlpatterns = [
    # http://http://127.0.0.1:8000/Apprenticeship/
    path('find_result/', views.find_result, name='find_result'),
    path('find_result/<str:question>', views.findResultQFromUrl, name='find_result_q_from_url'),
    path('draw_picture/<int:age_data1>/<int:age_data2>/<int:age_data3>/<int:age_data4>/<int:date_data1>/<int'
         ':date_data2>/<int:date_data3>/<int:date_data4>/<int:date_data5>/<int:date_data6>/<int:sex_data1>/<int'
         ':sex_data2>', views.draw_picture, name='draw_picture'),
    path('draw_picture_trend/<int:age_data1>/<int:age_data2>/<int:age_data3>/<int:age_data4>/<int:date_data1>/<int'
         ':date_data2>/<int:date_data3>/<int:date_data4>/<int:date_data5>/<int:date_data6>/<int:sex_data1>/<int'
         ':sex_data2>', views.draw_picture_trend, name='draw_picture_trend'),
    path('draw_picture_sex/<int:age_data1>/<int:age_data2>/<int:age_data3>/<int:age_data4>/<int:date_data1>/<int'
         ':date_data2>/<int:date_data3>/<int:date_data4>/<int:date_data5>/<int:date_data6>/<int:sex_data1>/<int'
         ':sex_data2>', views.draw_picture_sex, name='draw_picture_sex'),
]
