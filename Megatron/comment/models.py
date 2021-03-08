from django.db import models
from django.contrib.auth.models import User
from user.models import Department


# class Comment(models.Model):
#     content_object = models.ForeignKey(Homework, on_delete=models.DO_NOTHING)
#
#     text = models.TextField()
#     comment_time = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#
#     class Meta:
#         ordering = ['-comment_time']
#
#
# class Teacher_Comment(models.Model):
#     content_object = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
#
#     text = models.TextField()
#     comment_time = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#
#     class Meta:
#         ordering = ['-comment_time']


class questionsSearched(models.Model):
    questionsName = models.TextField()
    numSearched = models.IntegerField(default=0)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    timeFirstSearched = models.DateTimeField(auto_now_add = True)
    timeLastSearched = models.DateTimeField(auto_now=True)
