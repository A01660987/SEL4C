from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, "home.html")


def login_user(request):
    if(request.method == "POST"):
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user.is_superuser:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request,'Correo electrónico y/o contraseña inválidos.')
            return redirect('admin')
        
    return render(request, "login.html")


def about(request):
    return render(request, "about.html")


def aboutTeam(request):
    return render(request, "about-team.html")


def register(request):
    return render(request, "register.html")

@staff_member_required
def dashboard(request):
    return render(request, "dashboard.html")