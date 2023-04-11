from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Note, Todo
from datetime import date
from django.contrib.auth.decorators import login_required


# Create your views here.
# def welcome(request):
#     return render(request, "signup.html")

# def login(request):
#     pass

# def signup(request):
#     pass

@login_required
def note_home(request):
    title = Note.objects.filter(user=request.user)

    return render(request, "note.html", {"title":title})


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

    return render(request, "note_view.html", {"title":title})


@login_required
def note_delete(request, pk):
    title = Note.objects.filter(pk=pk, user=request.user).first()
    title.delete()

    messages.info(request, "Note Deleted Successfully")

    return redirect('/note/')


@login_required
def todo_home(request):
    todo = Todo.objects.filter(user=request.user)
    start = Todo.objects.filter(user=request.user)
    deadline = Todo.objects.filter(user=request.user)

    return render(request, "todo.html", {"todo": todo, "start": start, "deadline": deadline})


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
            Todo.objects.create(todo=todo, start=start, deadline=deadline, user=user)

        messages.success(request, "To-Do List Has Been Added Successfully")

        return redirect('/todo/')
    return render(request, "todo.html")

def todo_is_completed(request, pk):
        pass
