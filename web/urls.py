from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login_user"),
    path("about/", views.about, name="about"),
    path("about/team", views.aboutTeam, name="aboutTeam"),
    path("register/", views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
