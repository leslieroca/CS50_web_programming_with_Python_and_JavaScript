from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html") 

def leslie(request):
    return HttpResponse("Hello Leslie!")
 
 def greet(request, name):
    return render(request, "hello/greet.htm", {
        "name": name.capitalize()
    })