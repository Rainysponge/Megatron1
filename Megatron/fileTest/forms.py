from django import forms
from django.contrib import auth
from django.contrib.auth.models import User


class describeFrom(forms.Form):
    # 用于文本格式化
    describeText = forms.CharField(label='描述', widget=forms.Textarea(attrs={
                                        'style': 'height: 350px; width:480px'}),
                                   )
