from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class firstFileContent(models.Model):
    firstField = models.CharField(max_length=16)
    secondField = models.TextField()


class table_format(models.Model):
    # This models will never be created after first created!
    result_id = models.CharField(max_length=160, default='result_id', verbose_name="结果编号字典")
    patient_id = models.CharField(max_length=160, default='patient_id', verbose_name="患者编号字典")
    result_comment = models.CharField(max_length=160, default='result_comment', verbose_name="患者状况字典")  # 好转/无变化/恶化
    enabled = models.CharField(max_length=160, default='enabled', verbose_name="有效字典")
    deleted = models.CharField(max_length=160, default='deleted', verbose_name="无效字典")
    created_time = models.CharField(max_length=160, default='created_time', verbose_name="入院时间字典")
    updated_time = models.CharField(max_length=160, default='updated_time', verbose_name="出院时间字典")
    treatment_id = models.CharField(max_length=160, default='treatment_id', verbose_name="诊疗方法编号字典")

    treatment_name = models.CharField(max_length=160, default='treatment_name', verbose_name="诊疗方法字典")
    comment = models.CharField(max_length=160, default='comment', verbose_name="诊疗评论字典")  # 同上 两个comment没啥用
    illness_id = models.CharField(max_length=160, default='illness_id', verbose_name="疾病编号字典")

    illness_name = models.CharField(max_length=160, default='illness_name', verbose_name="疾病名字典")
    blood_sugar = models.CharField(max_length=160, default='blood_sugar', verbose_name="患者血糖字典")
    blood_pressure = models.CharField(max_length=160, default='blood_pressure', verbose_name="患者血压字典")
    blood_fat = models.CharField(max_length=160, default='blood_fat', verbose_name="患者血脂字典")
    department_id = models.CharField(max_length=160, default='department_id', verbose_name="科室编号字典")

    department_name = models.CharField(max_length=160, default='department_name', verbose_name="科室名字典")
    department_address = models.CharField(max_length=160, default='department_address', verbose_name="科室地址字典")
    patient_name = models.CharField(max_length=160, default='patient_name', verbose_name="患者姓名字典")
    gender = models.CharField(max_length=160, default='gender', verbose_name="性别字典")
    birth = models.CharField(max_length=160, default='birth', verbose_name="生日字典")  # 我看学长没用datetime
    age = models.CharField(max_length=160, default='age', verbose_name="年龄字典")


class Patient_Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Patient_info_id = models.CharField(max_length=6, null=True, blank=True)  # 就是patient_id
    heart_rate = models.CharField(max_length=6, null=True)
    weight = models.CharField(max_length=6, null=True)
    step_number = models.CharField(max_length=6, null=True)  # 步数
    sleep_time = models.CharField(max_length=6, null=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']

