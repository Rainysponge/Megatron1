from django.contrib import admin
from .models import questionsSearched
# Register your models here.


@admin.register(questionsSearched)
class questionsSearchedAdmin(admin.ModelAdmin):
    list_display = ('questionsName', 'numSearched', 'department', 'timeLastSearched')





