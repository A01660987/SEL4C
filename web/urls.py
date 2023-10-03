from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    path("about", views.about, name="about"),
    path("about/team", views.aboutTeam, name="aboutTeam"),
    path("register", views.register, name="register"),
    path("dashboard/", views.admin_panel, name="admin_panel"),
]
