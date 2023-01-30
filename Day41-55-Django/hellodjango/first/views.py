from django.shortcuts import render
from django.http import HttpResponse
from random import sample

# Create your views here.
def show_index(request):
    fruits = [
        "Apple",
        "Orange",
        "Pitaya",
        "Durian",
        "Waxberry",
        "Blueberry",
        "Grape",
        "Peach",
        "Pear",
        "Banana",
        "Watermelon",
        "Mango",
    ]
    selected_fruits = sample(fruits, 3)
    return render(request, "index.html", {"fruits": selected_fruits})
