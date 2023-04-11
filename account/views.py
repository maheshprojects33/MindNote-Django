from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Bio
from core.models import Note, Todo
from django.contrib import messages
from .forms import BioForm


def signup(request):
    bioform = BioForm
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.info(request, "Password Not Matched")
        
        if User.objects.filter(email=email.lower()).exists():
            messages.info(request, "User Already Exist")
            return redirect('login')

        else:
            user = User()
            user.full_name = full_name
            user.email = email.lower()
            user.password = make_password(password1)
            user.save()

            user_bio = Bio(user=user)
            user_bio.save()

            messages.info(request, "New User Created Successfully")

            return redirect('login')

    return render(request, 'signup.html', {"form": bioform})


def login_user(request):
    bioform = BioForm
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password1']
        
        user = authenticate(request, email=email.lower(), password=password)

        if user is not None:
            login(request, user) 
            return redirect('home')
        else:
            messages.info(request, "Either Username or Password Doesn't Matched")
            return redirect('login')

    return render(request, 'login.html', {"form": bioform})


def logout_user(request):
    logout(request)
    messages.info(request, "Loggedout Successfully")
    return redirect('login')
    
def home(request):
    title = Note.objects.filter(user=request.user)
    title_num = len(title)
    todo = Todo.objects.filter(user=request.user)
    todo_num = len(todo)

    return render(request, "home.html", {"title_num": title_num, "todo_num": todo_num})


@ login_required
def bio_view(request):
    bio = Bio.objects.filter(user=request.user).first()

    return render(request, "bio.html", {"bio": bio})

@ login_required
def bio_update(request):
    user = Bio.objects.filter(user=request.user).first()

    if request.method == "POST":
        update_address = request.POST.get('address')
        update_phone = request.POST.get('phone')
        update_country = request.POST.get('country')
        update_dob = request.POST.get('dob')
        
        user.address = update_address
        user.phone = update_phone
        user.country = update_country
        user.date_of_birth = update_dob

        user.save()

        messages.success(request, "Information Has Been Updated")

        return redirect('bio')
    
    return render(request, "bio.html")
