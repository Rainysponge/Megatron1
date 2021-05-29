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
    path('uploadFile_t_result_format/', views.tResultSubmit, name='uploadFile_t_result'),
    path('uploadFile_t_department_format/', views.tDepartmentSubmit, name='uploadFile_t_department'),
    path('uploadFile_t_patient_format/', views.tPatientSubmit, name='uploadFile_t_patient'),
    path('uploadFile_t_treatment_format/', views.tTreatmentSubmit, name='uploadFile_t_treatment'),
    path('uploadFile_t_illness_format/', views.tIllnessSubmit, name='uploadFile_t_illness'),
    path('patientUpdateData/', views.patientUpdateData, name='patientUpdateData'),
    path('showPatientData/', views.showPatientData, name='showPatientData'),
    path('docSearchPatientDaily/', views.docSearchPatientDaily, name='docSearchPatientDaily'),

]


