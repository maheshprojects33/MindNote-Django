from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Note, Todo
from datetime import date
from django.contrib.auth.decorators import login_required
import datetime


@login_required
def note_home(request):
    title = Note.objects.filter(user=request.user)

    return render(request, "note.html", {"title": title})


@login_required
def note_add(request):
    if request.method == "POST":
        title = request.POST['title']
        note = request.POST['note']
        user = request.user

        Note.objects.create(title=title, note=note, user=user)

        messages.success(request, "Note Added Successfully")

        return redirect('/note/')

    return render(request, "note_add.html")


@login_required
def note_edit(request, pk):
    title = Note.objects.filter(pk=pk, user=request.user).first()

    if request.method == "POST":
        new_title = request.POST['title']
        new_note = request.POST['note']

        title.title = new_title
        title.note = new_note

        title.save()

        messages.success(request, "Note Updated Successfully")

        return redirect('/note/')

    return render(request, "note_edit.html", {"title": title})


@login_required
def note_view(request, pk):
    title = Note.objects.filter(pk=pk, user=request.user).first()
    if request.method == "POST":
        return redirect("/note/")

    return render(request, "note_view.html", {"title": title})


@login_required
def note_delete(request, pk):
    title = Note.objects.filter(pk=pk, user=request.user).first()
    title.delete()

    messages.info(request, "Note Deleted Successfully")

    return redirect('/note/')


@login_required
def todo_home(request):
    todo_display = Todo.objects.filter(user=request.user).order_by('-is_completed')

    return render(request, "todo.html", {"todo_display": todo_display})


@login_required
def todo_add(request):
    if request.method == "POST":
        todo = request.POST['todo']
        start = request.POST['start']
        deadline = request.POST['deadline']
        user = request.user

        if not start and not deadline:
            Todo.objects.create(todo=todo, user=user)
        elif not deadline:
            Todo.objects.create(todo=todo, start=start, user=user)
        elif not start:
            Todo.objects.create(todo=todo, deadline=deadline, user=user)
        else:
            Todo.objects.create(todo=todo, start=start,
                                deadline=deadline, user=user)

        messages.success(request, "To-Do List Has Been Added Successfully")

        return redirect('/todo/')
    return render(request, "todo.html")


@login_required
def todo_edit(request, pk):
    todo = Todo.objects.filter(pk=pk, user=request.user).first()
    if request.method == 'POST':
        new_todo = request.POST.get('todo')
        new_start = request.POST.get('start')
        new_deadline = request.POST.get('deadline')

        if not new_start:
            todo.start = None
        if not new_deadline:
            todo.deadline = None

        todo.todo = new_todo
        todo.start = new_start if new_start else todo.start
        todo.deadline = new_deadline if new_deadline else todo.deadline

        todo.save()

        messages.success(request, "ToDo is updated Successfully")

        return redirect('/todo/')

    return render(request, "todo_edit.html", {"todo": todo})


@login_required
def todo_delete(request, pk):
    todo = Todo.objects.filter(pk=pk, user=request.user).first()
    todo.delete()

    messages.info(request, "List has been Deleted Successfully")

    return redirect("/todo/")



@login_required
def todo_is_completed(request):
    checked_todos = request.POST.getlist('checked_todos')
    print(checked_todos)
    
    for checked_todo in checked_todos:
        todo = Todo.objects.get(id=checked_todo)
        
        if todo.is_completed == False:
            todo.is_completed = True
            
            todo.save()
        else:
            todo.is_completed = False
            todo.save()
    messages.info(request, "Todo Has Been Updated")

    return redirect("/todo/")
