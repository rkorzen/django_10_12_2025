from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo


def list(request):
    # pobieram z bazy
    todos = Todo.objects.all()
    if q := request.GET.get("q"):
        todos = todos.filter(title__icontains=q)

    context = {
            "todos": todos,
        }

    return render(
        request,
        "todos/list.html",
        context
    )

def detail(request, id):

    todo = Todo.objects.get(id=id)
    context = {"todo": todo}

    return render(
        request,
        "todos/details.html",
        context
    )

def add(request):
    return HttpResponse("Dodanie oferty")
