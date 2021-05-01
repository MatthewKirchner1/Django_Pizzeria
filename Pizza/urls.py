from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "Pizza"

urlpatterns = [
    path("", views.index, name="index"),
    path("pizzas", views.pizzas, name="pizzas"),
    path("pizzas/<int:pizza_id>", views.pizza, name="pizza"),
]
