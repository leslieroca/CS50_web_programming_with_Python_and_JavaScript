from django import forms
from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

# Create froms using Django way
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })