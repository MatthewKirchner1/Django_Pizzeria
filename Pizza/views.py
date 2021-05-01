from django.shortcuts import render
from .models import Pizza, Topping

# Create your views here.


def index(request):
    """The home page"""
    return render(request, "Pizza/index.html")


def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {"pizzas": pizzas}
    return render(request, "Pizza/pizzas.html", context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = Topping.objects.all().filter(pizza=pizza_id)
    context = {"pizza": pizza, "toppings": toppings}

    return render(request, "Pizza/pizza.html", context)
