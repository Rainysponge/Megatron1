from django.db import models
from user.models import Doctor, Profile, Patient


# Create your models here.

class MedicalCase(models.Model):
    case_id = models.CharField(max_length=6, null=True, blank=True)
    doc_id = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True, blank=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True, blank=True)
    solutions = models.TextField()

