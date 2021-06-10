from typing_extensions import Required
from django import forms
from django.db.models import fields
from .models import Img

class UploadImg(forms.ModelForm):
    class Meta:
        model = Img
        fields = '_all_'

        error_messages = {
            'title':{
                'required' : '必须为上传图片命名',
                'max_length' : '最大长度为64'
            }
            
        }