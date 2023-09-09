from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def aboutTeam(request):
    return render(request, 'about-team.html')