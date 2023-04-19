from django.urls import path
from . import views

urlpatterns = [
    path('note/', views.note_home, name="note"),
    path('note-add/', views.note_add, name="note-add"),
    path('note-edit/<int:pk>/', views.note_edit, name="note-edit"),
    path('note-view/<int:pk>/', views.note_view, name="note-view"),
    path('note-delete/<int:pk>/', views.note_delete, name="note-delete"),

    path('todo/', views.todo_home, name="todo"),
    path('todo-add/', views.todo_add, name="todo-add"),
    path('todo-edit/<int:pk>/', views.todo_edit, name="todo-edit"),
    path('todo-delete/<int:pk>/', views.todo_delete, name="todo-delete"),
    path('todo-complete/', views.todo_is_completed, name="todo-complete"),
]
