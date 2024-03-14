
from app1.models import Todo
from django import forms
from django.shortcuts import render


class TodosForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Wash my car', 'aria-label': 'Todo', 'aria-describedby': 'add-btn'}),
        }
