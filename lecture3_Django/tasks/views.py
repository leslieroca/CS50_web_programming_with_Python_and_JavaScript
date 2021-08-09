from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

tasks = []

# Create froms using Django way
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            # Get redirected to the Tasks page after submit a task.
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/index.html", {
                "form": form
            })

    # If request methos is "GET"
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })