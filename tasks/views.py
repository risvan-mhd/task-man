from django.views.decorators.http import require_POST, require_http_methods
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, render

from django_htmx.http import trigger_client_event

from .models import Task


def index(request: WSGIRequest) -> HttpResponse:
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
    }

    return render(request, "index.html", context)


@require_POST
def task_create(request: WSGIRequest) -> HttpResponse:
    name = request.POST.get("task_name", "")
    if name.strip() == "":
        return HttpResponseBadRequest("Task name is required.")

    Task.objects.create(name=name)
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
    }

    respose = render(request, "index.html#task-list", context)
    return trigger_client_event(respose, "clearTaskForm")


@require_http_methods(["DELETE"])
def task_delete(request: WSGIRequest, pk: int) -> HttpResponse:
    get_object_or_404(Task, pk=pk).delete()
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
    }

    return render(request, "index.html#task-list", context)
