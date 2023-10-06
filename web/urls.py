from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path("about/", views.about, name="about"),
    path("about/team", views.aboutTeam, name="aboutTeam"),
    path("dashboard/", views.dashboard, name="dashboard"),
]