from django.db import models


# Create your models here.

class firstFileContent(models.Model):
    firstField = models.CharField(max_length=16)
    secondField = models.TextField()
