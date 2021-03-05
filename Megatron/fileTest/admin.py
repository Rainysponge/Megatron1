from django.contrib import admin
from .models import firstFileContent


# Register your models here.

@admin.register(firstFileContent)
class firstFileContentAdmin(admin.ModelAdmin):
    list_display = ('firstField', 'secondField')
