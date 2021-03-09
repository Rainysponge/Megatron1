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
    questionsName = models.TextField(verbose_name="问题")
    numSearched = models.IntegerField(default=0, verbose_name="次数")
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, verbose_name="科室")
    timeFirstSearched = models.DateTimeField(auto_now_add=True, verbose_name="第一次被查询")
    timeLastSearched = models.DateTimeField(auto_now=True, verbose_name="最后一次被查询")


class thesis(models.Model):
    title = models.CharField(max_length=100)
    key_word = models.CharField(max_length=16)
    link = models.TextField()
