from django import forms
from user.models import Profile
from django.contrib import auth
from django.contrib.auth.models import User


class describeFrom(forms.Form):
    # 用于文本格式化
    describeText = forms.CharField(label='描述', widget=forms.Textarea(attrs={
        'style': 'height: 200px; width:480px'}),
                                   )
    describeFormat = forms.CharField(label='描述格式化', required=False, widget=forms.Textarea(attrs={
        'style': 'height: 250px; width:480px'}),
                                     )


class tResultSubmitForm(forms.Form):
    result_id = forms.CharField(label='结果编号',
                                max_length=30, min_length=2, required=False,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': '默认为result_id',
                                           }))
    patient_id = forms.CharField(label='患者编号',
                                 max_length=30, min_length=2, required=False,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': '默认为patient_id',
                                            }))
    result_comment = forms.CharField(label='患者状况',
                                     max_length=30, min_length=2, required=False,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': '默认为result_comment',
                                                }))
    enabled = forms.CharField(label='有效',
                              max_length=30, min_length=2, required=False,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '默认为enabled',
                                         }))

    deleted = forms.CharField(label='无效',
                              max_length=30, min_length=2, required=False,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '默认为deleted',
                                         }))
    created_time = forms.CharField(label='入院时间',
                                   max_length=30, min_length=2, required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '默认为created_time',
                                              }))
    updated_time = forms.CharField(label='出院时间',
                                   max_length=30, min_length=2, required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '默认为updated_time',
                                              }))


class tDepartmentSubmitForm(forms.Form):
    department_id = forms.CharField(label='科室编号',
                                    max_length=30, min_length=2, required=False,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control', 'placeholder': '默认为department_id',
                                               }))
    patient_id = forms.CharField(label='患者编号',
                                 max_length=30, min_length=2, required=False,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': '默认为patient_id',
                                            }))
    department_name = forms.CharField(label='科室名',
                                      max_length=30, min_length=2, required=False,
                                      widget=forms.TextInput(
                                          attrs={'class': 'form-control', 'placeholder': '默认为department_name',
                                                 }))
    department_address = forms.CharField(label='科室地址',
                                         max_length=30, min_length=2, required=False,
                                         widget=forms.TextInput(
                                             attrs={'class': 'form-control', 'placeholder': '默认为department_address',
                                                    }))
    enabled = forms.CharField(label='有效',
                              max_length=30, min_length=2, required=False,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '默认为enabled',
                                         }))

    deleted = forms.CharField(label='无效',
                              max_length=30, min_length=2, required=False,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '默认为deleted',
                                         }))
    created_time = forms.CharField(label='入院时间',
                                   max_length=30, min_length=2, required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '默认为created_time',
                                              }))
    updated_time = forms.CharField(label='出院时间',
                                   max_length=30, min_length=2, required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '默认为updated_time',
                                              }))


class tPatientSubmitForm(forms.Form):
    patient_id = forms.CharField(label='患者编号',
                                 max_length=30, min_length=2, required=False,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': '默认为patient_id',
                                            }))
    patient_name = forms.CharField(label='患者姓名',
                                   max_length=30, min_length=2, required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '默认为patient_name',
                                              }))
    gender = forms.CharField(label='性别',
                             max_length=30, min_length=2, required=False,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': '默认为gender',
                                        }))
    birth = forms.CharField(label='生日',
                            max_length=30, min_length=2, required=False,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': '默认为birth',
                                       }))
    age = forms.CharField(label='年龄',
                          max_length=30, min_length=2, required=False,
                          widget=forms.TextInput(
                              attrs={'class': 'form-control', 'placeholder': '默认为age',
                                     }))
    enabled = forms.CharField(label='有效',
                              max_length=30, min_length=2, required=False,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '默认为enabled',
                                         }))

    deleted = forms.CharField(label='无效',
                              max_length=30, min_length=2, required=False,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '默认为deleted',
                                         }))
    created_time = forms.CharField(label='入院时间',
                                   max_length=30, min_length=2, required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '默认为created_time',
                                              }))
    updated_time = forms.CharField(label='出院时间',
                                   max_length=30, min_length=2, required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '默认为updated_time',
                                              }))


class tTreatmentSubmitForm(forms.Form):
    treatment_id = forms.CharField(label='诊疗方法编号',
                                   max_length=30, min_length=2, required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '默认为treatment_id',
                                              }))
    patient_id = forms.CharField(label='患者编号',
                                 max_length=30, min_length=2, required=False,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': '默认为patient_id',
                                            }))
    treatment_name = forms.CharField(label='诊疗方法',
                                     max_length=30, min_length=2, required=False,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': '默认为treatment_name',
                                                }))
    comment = forms.CharField(label='诊疗评论',
                              max_length=30, min_length=2, required=False,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '默认为comment',
                                         }))

    enabled = forms.CharField(label='有效',
                              max_length=30, min_length=2, required=False,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '默认为enabled',
                                         }))

    deleted = forms.CharField(label='无效',
                              max_length=30, min_length=2, required=False,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '默认为deleted',
                                         }))
    created_time = forms.CharField(label='入院时间',
                                   max_length=30, min_length=2, required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '默认为created_time',
                                              }))
    updated_time = forms.CharField(label='出院时间',
                                   max_length=30, min_length=2, required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '默认为updated_time',
                                              }))


class tIllnessSubmitForm(forms.Form):
    illness_id = forms.CharField(label='疾病编号',
                                 max_length=30, min_length=2, required=False,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': '默认为illness_id',
                                            }))
    patient_id = forms.CharField(label='患者编号',
                                 max_length=30, min_length=2, required=False,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': '默认为patient_id',
                                            }))
    illness_name = forms.CharField(label='疾病名',
                                   max_length=30, min_length=2, required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '默认为illness_name',
                                              }))
    blood_sugar = forms.CharField(label='患者血糖',
                                  max_length=30, min_length=2, required=False,
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control', 'placeholder': '默认为blood_sugar',
                                             }))
    blood_pressure = forms.CharField(label='患者血压',
                                     max_length=30, min_length=2, required=False,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': '默认为blood_pressure',
                                                }))
    blood_fat = forms.CharField(label='患者血脂',
                                max_length=30, min_length=2, required=False,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': '默认为blood_fat',
                                           }))
    comment = forms.CharField(label='状况',
                              max_length=30, min_length=2, required=False,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '默认为comment',
                                         }))
    enabled = forms.CharField(label='有效',
                              max_length=30, min_length=2, required=False,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '默认为enabled',
                                         }))

    deleted = forms.CharField(label='无效',
                              max_length=30, min_length=2, required=False,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '默认为deleted',
                                         }))
    created_time = forms.CharField(label='入院时间',
                                   max_length=30, min_length=2, required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '默认为created_time',
                                              }))
    updated_time = forms.CharField(label='出院时间',
                                   max_length=30, min_length=2, required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '默认为updated_time',
                                              }))


class patientUpdateDataForm(forms.Form):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Patient_info_id = models.CharField(max_length=6, null=True, blank=True)  # 就是patient_id
    # heart_rate = models.CharField(max_length=6, null=True)
    # weight = models.CharField(max_length=6, null=True)
    # step_number = models.CharField(max_length=6, null=True)  # 步数
    # sleep_time = models.CharField(max_length=6, null=True)
    # time = models.DateTimeField(auto_now_add=True)
    heart_rate = forms.CharField(label='心率',
                                 max_length=30, min_length=2,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': '例如:75',
                                            }))
    weight = forms.CharField(label='体重',
                             max_length=30, min_length=2,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': '单位(kg)',
                                        }))
    step_number = forms.CharField(label='步数',
                                  max_length=30, min_length=2,
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control', 'placeholder': '例如:8888',
                                             }))

    sleep_time = forms.CharField(label='睡眠时间',
                                 max_length=30, min_length=1,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': '单位:(小时)',
                                            }))

    def clean_heart_rate(self):
        heart_rate = self.cleaned_data['heart_rate']
        try:
            heart_rate_int = int(heart_rate)
            if heart_rate_int < 10 or heart_rate_int > 160:
                raise forms.ValidationError("不是合法数字")
            return heart_rate
        except Exception as e:
            raise forms.ValidationError("不是合法数字")

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        try:
            weight_int = float(weight)
            if weight_int < 2 or weight_int > 160:
                raise forms.ValidationError("不是合法数字")
            return weight
        except Exception as e:
            raise forms.ValidationError("不是合法数字")

    def clean_sleep_time(self):
        sleep_time = self.cleaned_data['sleep_time']
        try:
            sleep_time_int = float(sleep_time)
            if sleep_time_int < 0 or sleep_time_int > 24:
                raise forms.ValidationError("不是合法数字")
            return sleep_time
        except Exception as e:
            raise forms.ValidationError("不是合法数字")

    def clean_step_number(self):
        step_number = self.cleaned_data['step_number']
        try:
            step_number_int = int(step_number)
            if step_number_int < 0:
                raise forms.ValidationError("不是合法数字")
            return step_number
        except Exception as e:
            raise forms.ValidationError("不是合法数字")


class searchPatientDailyForm(forms.Form):
    text = forms.CharField(widget=forms.widgets.Input(attrs={
        'class': 'form-control input-lg',
        'style': 'width:600px',

    }))

    # def clean_text(self):
    #     patientName = self.cleaned_data['text']
    #     profile = Profile.objects.filter(real_name__contains=patientName)
    #     if len(profile) == 0:
    #         raise forms.ValidationError("该用户不存在")
    #     else:
    #         return patientName
