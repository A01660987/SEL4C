from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
        elif user is not None:
            login(request, user)
            return redirect("student_dashboard")
        else:
            messages.error(request,'Correo electrónico y/o contraseña inválidos.')
            return redirect("login")
        
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


def about(request):
    return render(request, "about.html")


@staff_member_required()
def dashboard(request):
    user = User.objects.get(username=request.user.username)
    students = Student.objects.all().order_by('user__name')
    return render(request, "dashboard.html", {"user": user, "students": students,})

@login_required
def student_dashboard(request):
    if request.user.is_superuser:
        return redirect("dashboard")
    user = User.objects.get(username=request.user.username)
    student = Student.objects.get(user=user)
    return render(request, "student-dashboard.html", {"student": student,})