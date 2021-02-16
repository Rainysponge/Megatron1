from django import forms
from ckeditor.widgets import CKEditorWidget


class createCaseForm(forms.Form):
    patient_No = forms.CharField(label='病人编号',
                                 max_length=16, min_length=1,
                                 widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    disease = forms.CharField(label='病症',
                              max_length=30, min_length=2,
                              widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    solution = forms.CharField(label='解决方案',
                               max_length=30, min_length=1,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
