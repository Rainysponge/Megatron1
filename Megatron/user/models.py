from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Department(models.Model):
    Department_name = models.CharField(max_length=16)
    contends = models.TextField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    real_name = models.CharField(max_length=6, null=True, blank=True)
    sex = models.CharField(max_length=2, null=True, blank=True)

    birth = models.DateTimeField(null=True, blank=True)
    is_doc = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doc_id = models.CharField(max_length=6, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True, blank=True)
    is_active = models.BooleanField(default=True)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Patient_id = models.CharField(max_length=6, null=True, blank=True)
    is_active = models.BooleanField(default=True)
