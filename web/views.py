from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from SEL4C.models import *
from django.views.decorators.clickjacking import xframe_options_exempt

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
    data = []
    for student in students:
        progress = Answer.objects.filter(user=student.user).count()/ExerciseStep.objects.count() * 100
        data.append(progress)
    context = {
        "user": user,
        "students": zip(students, data),
    }
    return render(request, "dashboard.html", context)

@login_required
def student_dashboard(request):
    if request.user.is_superuser:
        return redirect("dashboard")
    user = User.objects.get(username=request.user.username)
    student = Student.objects.get(user=user)
    return render(request, "student-dashboard.html", {"student": student,})

@xframe_options_exempt
def student_gender_chart(request):
    labels = ["Masculino", "Femenino", "No binario", "Otro", "Prefiero no decir"]
    data = [Student.objects.filter(gender = 'M').count(), 
            Student.objects.filter(gender = 'F').count(),
            Student.objects.filter(gender = 'N').count(),
            Student.objects.filter(gender = 'O').count(),
            Student.objects.filter(gender = 'P').count()]
    return render(request, "barchart.html", {
        "labels": labels, 
        "data": data
    })

@xframe_options_exempt
def student_age_chart(request):
    age_list = list(Student.objects.values('age').all())
    ages = []
    age_students = []
    for age in age_list:
        ages.append(str(age['age']) + " años")
        age_students.append(Student.objects.filter(age = age['age']).count())

    labels = ages
    data = age_students
    return render(request, "barchart.html", {
        "labels": labels, 
        "data": data
    })

@xframe_options_exempt
def student_country_chart(request):
    country_list = list(Student.objects.values('country').all())

    countries = []
    for country in country_list:
        if country not in countries:
            countries.append(country)
            print(countries)

    country_list = countries

    countries = []
    country_students = []
    for country in country_list:
        if country['country'] not in countries:
            countries.append(country['country'])
        country_students.append(Student.objects.filter(country = country['country']).count())

    labels = countries
    data = country_students
    return render(request, "barchart.html", {
        "labels": labels, 
        "data": data
    })

@xframe_options_exempt
def student_degree_chart(request):
    degree_list = list(Degree.objects.values('id', 'type').all())
    degrees = []
    degree_students = []
    for degree in degree_list:
        degrees.append(degree['type'])
        degree_students.append(Student.objects.filter(studies__degree_id = degree['id']).count())

    labels = degrees
    data = degree_students
    return render(request, "piechart.html", {
        "labels": labels, 
        "data": data
    })

@xframe_options_exempt
def student_discipline_chart(request):
    discipline_list = list(Discipline.objects.values('id', 'name').all())
    disciplines = []
    discipline_students = []
    for discipline in discipline_list:
        disciplines.append(discipline['name'])
        discipline_students.append(Student.objects.filter(studies__discipline_id = discipline['id']).count())

    labels = disciplines
    data = discipline_students
    return render(request, "piechart.html", {
        "labels": labels, 
        "data": data
    })

@xframe_options_exempt
def student_institution_chart(request):
    institution_list = list(Institution.objects.values('id', 'name').all())
    institutions = []
    institution_students = []
    for institution in institution_list:
        institutions.append(institution['name'])
        institution_students.append(Student.objects.filter(studies__institution_id = institution['id']).count())

    labels = institutions
    data = institution_students
    return render(request, "piechart.html", {
        "labels": labels, 
        "data": data
    })

@xframe_options_exempt
def answer_activity_chart(request):
    # activity_list = list(Answer.objects.values('activity').all())
    activity_list = list(Activity.objects.values().all())
    answers = []
    print(activity_list)
    answer_activities = []
    for activity in activity_list:
        answers.append(activity['activity_number'])
        print(activity)
        print(answers)
        answer_activities.append(Answer.objects.filter(activity = activity['id']).count())
        print(answer_activities)

    print(activity_list)
    print(answer_activities)
    labels = answers
    data = answer_activities
    return render(request, "piechart.html", {
        "labels": labels, 
        "data": data
    })