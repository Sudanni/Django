from django import forms
from .models import *

class VerRepostoryForm(forms.ModelForm):
    class Meta:
        model = ver_repostory
        fields = "__all__"
        # exclude = ('email_issend', 'tags',)  # 排除哪个字段
        #fields = ['content', ] #指定哪些字段
    def __init__(self, *args, **kwargs):
        #  继承父类，后重写自己的类
        super(VerRepostoryForm, self).__init__(*args, **kwargs)

        for field_name in self.base_fields:   # 遍历每一个字段
            field = self.base_fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})  # 给每一个输入框添加上一个样式

class SerVersionForm(forms.ModelForm):
    class Meta:
        model = ser_version
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        #  继承父类，后重写自己的类
        super(SerVersionForm, self).__init__(*args, **kwargs)

        for field_name in self.base_fields:   # 遍历每一个字段
            field = self.base_fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})

class OpeDirectorForm(forms.ModelForm):
    class Meta:
        model = ope_director
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        #  继承父类，后重写自己的类
        super(OpeDirectorForm, self).__init__(*args, **kwargs)

        for field_name in self.base_fields:   # 遍历每一个字段
            field = self.base_fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})

