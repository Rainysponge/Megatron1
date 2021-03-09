from django.contrib import admin
from .models import questionsSearched, thesis
# Register your models here.


@admin.register(questionsSearched)
class questionsSearchedAdmin(admin.ModelAdmin):
    list_display = ('questionsName', 'numSearched', 'department', 'timeLastSearched')


@admin.register(thesis)
class thesisAdmin(admin.ModelAdmin):
    list_display = ('title', 'key_word', 'link')





