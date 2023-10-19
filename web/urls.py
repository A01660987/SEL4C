from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("about/", views.about, name="about"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),

    path("student_gender_chart/", views.student_gender_chart, name="student_gender_chart"),
    path("student_age_chart/", views.student_age_chart, name="student_age_chart"),
    path("student_country_chart/", views.student_country_chart, name="student_country_chart"),
    path("student_degree_chart/", views.student_degree_chart, name="student_degree_chart"),
    path("student_discipline_chart/", views.student_discipline_chart, name="student_discipline_chart"),
    path("student_institution_chart/", views.student_institution_chart, name="student_institution_chart"),
    path("answer_activity_chart/", views.answer_activity_chart, name="answer_activity_chart"),
]