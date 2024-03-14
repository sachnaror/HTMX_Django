import app1.views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1.views.index, name="index"),
    path('create-todo/', app1.views.create_todo, name="create_todo"),

]
