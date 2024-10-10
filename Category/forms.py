from django import forms
from Category.models import CategoryModel


class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = '__all__'
