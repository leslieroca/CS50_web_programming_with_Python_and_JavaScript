from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("leslie", views.leslie, name="leslie")
]
