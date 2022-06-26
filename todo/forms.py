from django.forms import ModelForm, CheckboxInput, TextInput
from .models import *
class ToDoForm(ModelForm):
    class Meta():
        model = TodoItem
        fields = ['complete', 'title', 'desc']
        widgets = {
            'complete': CheckboxInput(attrs={'class': 'form-check-input'}),
            'title': TextInput(attrs={
            "class": "form-control",
            "id":"exampleFormControlInput1"}),
            'desc': TextInput(attrs={
            "class": "form-control",
            "id":"exampleFormControlInput1"}),
        }

        
