from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from .models import Task


def index(request: WSGIRequest) -> HttpResponse:
    tasks = Task.objects.all()
    _ = tasks

    # Dummy data
    context = {
        "tasks": [
            {"name": "Task 1", "completed": True},
            {"name": "Task 2", "completed": False},
            {"name": "Task 3", "completed": False},
            {"name": "Task 4", "completed": False},
            {"name": "Task 5", "completed": False},
        ],
    }
    return render(request, "index.html", context)
