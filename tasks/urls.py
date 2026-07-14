from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("tasks/", views.task_create, name="task-create"),
    path("tasks/<int:pk>/", views.task_delete, name="task-delete"),
]
