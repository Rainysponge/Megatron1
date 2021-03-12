from django.db import models


class patient(models.Model):
    patient_id = models.CharField(max_length=100, verbose_name="患者编号")
    patient_name = models.CharField(max_length=100, verbose_name="患者姓名")
    gender = models.CharField(max_length=100, verbose_name="性别")
    birth = models.CharField(max_length=100, verbose_name="生日")    # 我看学长没用datetime
    age = models.IntegerField(default=0, verbose_name="年龄")
    enabled = models.IntegerField(default=0, verbose_name="有效")     # 其实没啥用
    deleted = models.IntegerField(default=0, verbose_name="无效")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="入院时间")
    updated_time = models.DateTimeField(auto_now_add=True, verbose_name="出院时间")

    def __str__(self):
        return self.patient_name


class department(models.Model):
    department_id = models.CharField(max_length=100, verbose_name="科室编号")
    patient_id = models.CharField(max_length=100, default=0, verbose_name="患者编号")
    # patient = models.ForeignKey(patient, on_delete=models.DO_NOTHING)
    department_name = models.CharField(max_length=100, verbose_name="科室名")
    department_address = models.CharField(max_length=100, verbose_name="科室地址")
    enabled = models.IntegerField(default=0, verbose_name="有效")
    deleted = models.IntegerField(default=0, verbose_name="无效")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="入院时间")
    updated_time = models.DateTimeField(auto_now_add=True, verbose_name="出院时间")

    def __str__(self):
        return self.department_name


class illness(models.Model):
    illness_id = models.CharField(max_length=100, verbose_name="疾病编号")
    patient_id = models.CharField(max_length=100, default=0, verbose_name="患者编号")
    # patient = models.ForeignKey(patient, on_delete=models.DO_NOTHING)
    illness_name = models.CharField(max_length=100, verbose_name="疾病名")
    blood_sugar = models.CharField(max_length=100, verbose_name="患者血糖")
    blood_pressure = models.CharField(max_length=100, verbose_name="患者血压")
    blood_fat = models.CharField(max_length=100, verbose_name="患者血脂")
    comment = models.CharField(max_length=100, verbose_name="状况")   # 原指状况 不过与result重复 没多少用
    enabled = models.IntegerField(default=0, verbose_name="有效")
    deleted = models.IntegerField(default=0, verbose_name="无效")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="入院时间")
    updated_time = models.DateTimeField(auto_now_add=True, verbose_name="出院时间")

    def __str__(self):
        return self.illness_name


class result(models.Model):
    result_id = models.CharField(max_length=100, verbose_name="结果编号")
    patient_id = models.CharField(max_length=100, default=0, verbose_name="患者编号")
    # patient = models.ForeignKey(patient, on_delete=models.DO_NOTHING)   # 会生成patient_id 十分诡异
    result_comment = models.CharField(max_length=100, verbose_name="患者状况")  # 好转/无变化/恶化
    enabled = models.IntegerField(default=0, verbose_name="有效")
    deleted = models.IntegerField(default=0, verbose_name="无效")
    created_time = models.DateTimeField(verbose_name="入院时间")
    updated_time = models.DateTimeField(verbose_name="出院时间")
    # enabled = models.CharField(max_length=1, default=0)
    # deleted = models.CharField(max_length=1, default=0)
    # created_time = models.DateTimeField(auto_now_add=True)
    # updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.result_comment


class treatment(models.Model):
    treatment_id = models.CharField(max_length=100, verbose_name="诊疗方法编号")
    patient_id = models.CharField(max_length=100, default=0, verbose_name="患者编号")
    # patient = models.ForeignKey(patient, on_delete=models.DO_NOTHING)
    # 直接定义patient_id不用外键 patient_id =
    treatment_name = models.CharField(max_length=100, verbose_name="诊疗方法")
    comment = models.CharField(max_length=100, verbose_name="诊疗评论") # 同上 两个comment没啥用
    enabled = models.IntegerField(default=0, verbose_name="有效")
    deleted = models.IntegerField(default=0, verbose_name="无效")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="入院时间")
    updated_time = models.DateTimeField(auto_now_add=True, verbose_name="出院时间")

    def __str__(self):
        return self.treatment_name

