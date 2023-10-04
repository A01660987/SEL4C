from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, "home.html")


def login(request):
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