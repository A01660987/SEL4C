from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
import SEL4C.permissions as permissions

class User(AbstractUser):
    first_name = None
    last_name = None
    # El username es el correo electrónico, sin embargo Django requiere que cada usuario tenga un campo llamado específicamente "username".
    username = models.EmailField(unique=True, verbose_name="Correo electrónico")
    name = models.CharField(max_length=150, verbose_name="Nombre(s)")
    first_lastname = models.CharField(max_length=150, verbose_name="Apellido paterno")
    second_lastname = models.CharField(max_length=150, verbose_name="Apellido materno")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    
    REQUIRED_FIELDS = [
        'name',
        'first_lastname',
        'second_lastname',
    ]

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Institution(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Institución")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Institución"
        verbose_name_plural = "Instituciones"
        ordering = ["name"]

class Discipline(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Disciplina")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"
        ordering = ["name"]

class Degree(models.Model):
    DEGREE_TYPES = [
        ('L', 'Licenciatura'),
        ('M', 'Maestría'),
        ('D', 'Doctorado'),
    ]
    type = models.CharField(max_length=1, choices=DEGREE_TYPES, verbose_name="Tipo")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Disciplina")
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, verbose_name="Institución")
    name = models.CharField(max_length=100, verbose_name="Título")
    acronym = models.CharField(max_length=10, verbose_name="Siglas")

    def __str__(self):
        return self.name + ", " + self.institution.name
    
    class Meta:
        verbose_name = "Título académico"
        verbose_name_plural = "Títulos académicos"
        ordering = ["institution", "discipline", "type"]

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(130)], verbose_name="Edad")
    agreed_policies = models.BooleanField(default=True, verbose_name="¿Acepta las políticas de privacidad?", validators=[permissions.is_agreed_on_policy])
    
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('N', 'No binario'),
        ('O', 'Otro'),
        ('P', 'Prefiero no decir'),
    ]
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Género")
    country = CountryField(verbose_name="País")
    degree = models.OneToOneField(Degree, on_delete=models.CASCADE, verbose_name="Título académico")
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, verbose_name="Degree")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Discipline")
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, verbose_name="Institution")

    REQUIRED_FIELDS = [
        'age',
        'agreed_policies',
    ]

    def __str__(self):
        return self.user.name + " " + self.user.first_lastname + " " + self.user.second_lastname

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ["user"]


"""Holds the title for an activity. Through the country field different languages are possible for the future"""
class ActivityText(models.Model):
    title = models.TextField( verbose_name="Title")
    country = CountryField(verbose_name="País")

    def __str__(self):
        return "Activity" + self.title
    
    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
        ordering = ["title"]


"""An activity is the title for a group of exercise steps. E.g. name = 'Identification' displays at the main screen and is connected to 4 exercise steps"""
class Activity(models.Model):
    activity_number = models.PositiveSmallIntegerField(verbose_name="Number of activity")
    activity_text = models.ForeignKey(ActivityText, on_delete=models.CASCADE, verbose_name="Activity text")

    def __str__(self):
        return "Activity" + self.activity_number
    
    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
        ordering = ["activity_number"]


"""An exercise step is created when an answer to an exercise is necessary. E.g. 3 in-app screens of instructions and an upload form afterwards form one exercise step"""
class ExerciseStep(models.Model):
    exerciseStep_number = models.PositiveSmallIntegerField(verbose_name="Number of exercise")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name="Activity")

    def __str__(self):
        return "Exercise" + self.exerciseStep_number + ", Activity" + self.activity
    
    class Meta:
        verbose_name = "Exercise"
        verbose_name_plural = "Exercises"
        ordering = ["exerciseStep_number"]


class AnswerUpload(models.Model):
    link = models.TextField(verbose_name="File link")
    filename = models.TextField(verbose_name="File name")

    def __str__(self):
        return "Upload name " + self.filename
    
    class Meta:
        verbose_name = "Upload"
        verbose_name_plural = "Uploads"

class AnswerText(models.Model):
    text = models.TextField(verbose_name="Answer")

    def __str__(self):
        return "Answer: " + self.answer[:10] # first 10 characters of answer
    
    class Meta:
        verbose_name = "Text answer"
        verbose_name_plural = "Text answers"

class AnswerRating(models.Model):
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Rating")

    def __str__(self):
        return "Rating: " + self.answer
    
    class Meta:
        verbose_name = "Rating answer"
        verbose_name_plural = "Rating answers"


"""An answer can be of 3 types and can only be one at the same time. Other Foreign Keys are in this case NULL. Answer-FK are initialized with NULL and not required"""
class Answer(models.Model):

    ANSWER_TYPES = [
        ('U', 'Upload'),
        ('T', 'Text'),
        ('R', 'Rating'),
    ]

    type = models.CharField(max_length=1, choices=ANSWER_TYPES, verbose_name="Tipo")
    upload_answer = models.ForeignKey(AnswerUpload, on_delete=models.CASCADE, verbose_name="Upload", null=True, blank=True)
    text_answer = models.ForeignKey(AnswerText, on_delete=models.CASCADE, verbose_name="Text", null=True, blank=True)
    rating_answer = models.ForeignKey(AnswerRating, on_delete=models.CASCADE, verbose_name="Rating", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    exercise = models.ForeignKey(ExerciseStep, on_delete=models.CASCADE, verbose_name="Exercise")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name="Activity")
    submitted = models.DateTimeField(auto_now=True, verbose_name="Fecha de submit")

    def __str__(self):
        return "Answer of type" + self.type + ", Student " + self.student
    
    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        ordering = ["submitted"]
        