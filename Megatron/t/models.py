from django.db import models


class patient(models.Model):
    patient_id = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    birth = models.CharField(max_length=100)    # 我看学长没用datetime
    age = models.IntegerField(default=0)
    enabled = models.IntegerField(default=0)
    deleted = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name


class department(models.Model):
    department_id = models.CharField(max_length=100)
    patient = models.ForeignKey(patient, on_delete=models.DO_NOTHING)
    department_name = models.CharField(max_length=100)
    department_address = models.CharField(max_length=100)
    enabled = models.IntegerField(default=0)
    deleted = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.department_name


class illness(models.Model):
    illness_id = models.CharField(max_length=100)
    patient = models.ForeignKey(patient, on_delete=models.DO_NOTHING)
    illness_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    enabled = models.IntegerField(default=0)
    deleted = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.illness_name


class result(models.Model):
    result_id = models.CharField(max_length=100)
    patient = models.ForeignKey(patient, on_delete=models.DO_NOTHING)   # 会生成patient_id 十分诡异
    result_comment = models.CharField(max_length=100)
    enabled = models.IntegerField(default=0)
    deleted = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.result_comment


class treatment(models.Model):
    treatment_id = models.CharField(max_length=100)
    patient = models.ForeignKey(patient, on_delete=models.DO_NOTHING)
    treatment_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    enabled = models.IntegerField(default=0)
    deleted = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.treatment_name

