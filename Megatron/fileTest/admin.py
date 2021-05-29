from django.contrib import admin
from .models import firstFileContent, table_format, Patient_Information


# Register your models here.

@admin.register(firstFileContent)
class firstFileContentAdmin(admin.ModelAdmin):
    list_display = ('firstField', 'secondField')


@admin.register(table_format)
class table_formatAdmin(admin.ModelAdmin):
    list_display = ('result_id', 'patient_id')


@admin.register(Patient_Information)
class Patient_InformationAdmin(admin.ModelAdmin):
    list_display = ('user', 'time')
