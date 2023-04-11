from django.db import models
from django.conf import settings


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=50)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Todo(models.Model):
    todo = models.CharField(max_length=100)
    start = models.DateField(blank=True, null=True, default=None)
    deadline = models.DateField(blank=True, null=True, default=None)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
