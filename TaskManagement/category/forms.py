from .models import *
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
    