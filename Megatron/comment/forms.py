# form表单 内容与前端form的name="text"交互
from django import forms
from ckeditor.widgets import CKEditorWidget


# class CommentForm(forms.Form):
#     homework_id = forms.IntegerField(widget=forms.HiddenInput)
#     text = forms.CharField(widget=CKEditorWidget())
#
#
# class Teacher_CommentForm(forms.Form):
#     teacher_id = forms.IntegerField(widget=forms.HiddenInput)
#     text = forms.CharField(widget=CKEditorWidget()) # config_name='teacher_comment_ckeditor')


class Search_Comment(forms.Form):
    text = forms.CharField(widget=forms.widgets.Input(attrs={
        'class': 'form-control input-lg', 'style': 'width:700px'}))
