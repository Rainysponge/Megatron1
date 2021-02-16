from django.contrib import admin
from .models import *


@admin.register(patient)
class patientAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_id', 'patient_name', 'gender', 'birth', 'age', 'enabled', 'deleted', 'created_time', 'updated_time')


@admin.register(department)
class patientAdmin(admin.ModelAdmin):
    list_display = ('id', 'department_id', 'patient_id', 'department_name', 'department_address', 'enabled', 'deleted', 'created_time', 'updated_time')


@admin.register(illness)
class illnessAdmin(admin.ModelAdmin):
    list_display = ('id', 'illness_id', 'patient_id', 'illness_name', 'comment', 'enabled', 'deleted', 'created_time', 'updated_time')


@admin.register(result)
class resultAdmin(admin.ModelAdmin):
    list_display = ('id', 'result_id', 'patient_id', 'result_comment', 'enabled', 'deleted', 'created_time', 'updated_time')


@admin.register(treatment)
class treatmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'treatment_id', 'patient_id', 'treatment_name', 'comment', 'enabled', 'deleted', 'created_time', 'updated_time')
