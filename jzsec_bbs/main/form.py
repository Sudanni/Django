from django import forms
from .models import *


class DiscussForm(forms.ModelForm):
    class Meta:
        model = Discuss
        fields = ['content',]

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"