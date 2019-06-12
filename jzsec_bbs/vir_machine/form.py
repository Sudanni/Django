from django import forms
from .models import *


class virmachineForm(forms.ModelForm):
    class Meta:
        model = vir_machine
        fields = "__all__"