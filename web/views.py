from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from SEL4C.models import *


def home(request):
    return render(request, "home.html")


def login_view(request):
    if(request.method == "POST"):
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request,'Correo electrónico y/o contraseña inválidos.')
            return redirect("login")
        
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


def about(request):
    return render(request, "about.html")


def about_team(request):
    return render(request, "about-team.html")


@staff_member_required()
def dashboard(request):
    user = User.objects.get(username=request.user.username)
    students = Student.objects.all()
    return render(request, "dashboard.html", {"user": user, "students": students,})