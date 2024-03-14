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
    if request.method == "POST":
        form = TodosForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return render(request, "todo_partial.html", {"todo": todo})

    return render(request, "todo_form.html", {"form": TodosForm})
