# myapp/views.py

from app1.forms import TodosForm
from app1.models import Todo
from django.shortcuts import render

# myapp/views.py


def index(request):
    context = {"form": TodosForm, "todos": Todo.objects.all()}
    return render(request, "index.html", context)
# myapp/views.py


def create_todo(request):
    form = TodosForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "todo_partial.html", {"form": form})
