from django.shortcuts import render, redirect
from .models import Pizza, Topping, Comment
from .forms import CommentForm

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
    comments = Comment.objects.all().filter(pizza=pizza_id)
    context = {"pizza": pizza, "toppings": toppings, "comments": comments}

    return render(request, "Pizza/pizza.html", context)


def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != "POST":
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)

            new_comment.pizza = pizza
            new_comment.save()
            form.save()
            return redirect("Pizza:pizza", pizza_id=pizza_id)

    context = {"form": form, "pizza": pizza}
    return render(request, "Pizza/new_comment.html", context)
