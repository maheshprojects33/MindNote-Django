from django.contrib import admin
from .models import *

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ["title", "note", "user"]

admin.site.register(Note, NoteAdmin)

class TodoAdmin(admin.ModelAdmin):
    list_display = ['todo', 'start', 'deadline', 'is_completed', 'id', "user"]

admin.site.register(Todo, TodoAdmin)