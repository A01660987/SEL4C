from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("about/", views.about, name="about"),
    path("about/team", views.about_team, name="about_team"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
]