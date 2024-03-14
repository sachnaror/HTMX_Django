# Django + HTMX: Superpower Your HTML Templates

This repository demonstrates how to integrate HTMX with Django to add interactivity to HTML templates easily.

## Introduction

HTMX is a powerful tool for adding interactivity to HTML templates without the complexity of JavaScript frameworks like React or Vue. This repository provides a step-by-step guide on how to leverage HTMX with Django to create dynamic web applications.

## Getting Started

Follow these steps to set up the project:

1. **Create a project**: Start a new Django project.

   ```bash
   pip install Django
   python -m django startproject django_htmx .
   python manage.py startapp myapp
Install dependencies: Install HTMX for Django.

bash
Copy code
pip install django-htmx
Database: This project uses Supabase (Postgres) for the database. Follow the provided tutorial to set up the project.

Models: Define models for the application.

python
Copy code


# myapp/models.py

from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100)
Forms: Create forms for data input.

python
Copy code


# myapp/forms.py

from django import forms
from myapp.models import Todo

class TodosForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("name",)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"})
        }
Migrations: Apply database migrations.

bash
Copy code
python manage.py makemigrations myapp
python manage.py migrate
Views: Define views for rendering templates and processing requests.

python
Copy code


# myapp/views.py

from django.shortcuts import render
from myapp.forms import TodosForm
from myapp.models import Todo

def index(request):
    context = {"form": TodosForm, "todos": Todo.objects.all()}
    return render(request, "index.html", context)
URLs: Configure URLs for the project.

python
Copy code


# django_htmx/urls.py


from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name="index"),
]
Templates: Create HTML templates for rendering views.

todo_form.html
todo_partial.html
index.html
Usage
Run Server: Start the Django development server.

bash
Copy code
python manage.py runserver
