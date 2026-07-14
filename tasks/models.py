from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=256)
    competed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
