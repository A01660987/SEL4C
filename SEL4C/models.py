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
    name = models.CharField(max_length=100, verbose_name="Título")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Título académico"
        verbose_name_plural = "Títulos académicos"
        ordering = ["name"]


"""Holds every combination of Institution, Discipline and Degree offered by a Institution"""
class AvailableStudies(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, verbose_name="Institución")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Disciplina")
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, verbose_name="Título académico")

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "Estudio disponible"
        verbose_name_plural = "Esudios disponibles"
        ordering = ["institution"]

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
    studies = models.ForeignKey(AvailableStudies, on_delete=models.CASCADE, verbose_name="Studies")

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
    title = models.TextField( verbose_name="Título")
    country = CountryField(verbose_name="País")

    def __str__(self):
        return "Título de actividad: " + self.title
    
    class Meta:
        verbose_name = "Título de actividad"
        verbose_name_plural = "Títulos de actividad"
        ordering = ["title"]


"""An activity is the title for a group of exercise steps. E.g. name = 'Identification' displays at the main screen and is connected to 4 exercise steps"""
class Activity(models.Model):
    activity_number = models.PositiveSmallIntegerField(verbose_name="Número de actividad")
    activity_text = models.ForeignKey(ActivityText, on_delete=models.CASCADE, verbose_name="Texto de actividad")

    def __str__(self):
        return "Actividad: " + self.activity_number
    
    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["activity_number"]


"""An exercise step is created when an answer to an exercise is necessary. E.g. 3 in-app screens of instructions and an upload form afterwards form one exercise step"""
class ExerciseStep(models.Model):
    exerciseStep_number = models.PositiveSmallIntegerField(verbose_name="Número de ejercicio")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name="Actividad")

    def __str__(self):
        return "Ejercicio: " + self.exerciseStep_number + ", Actividad: " + self.activity
    
    class Meta:
        verbose_name = "Ejercicio"
        verbose_name_plural = "Ejercicios"
        ordering = ["exerciseStep_number"]


class AnswerUpload(models.Model):
    link = models.TextField(verbose_name="Link al archivo")
    filename = models.TextField(verbose_name="Nombre del archivo")

    def __str__(self):
        return "Nombre del archivo: " + self.filename
    
    class Meta:
        verbose_name = "Carga de archivo"
        verbose_name_plural = "Cargas de archivo"

class AnswerText(models.Model):
    text = models.TextField(verbose_name="Respuesta")

    def __str__(self):
        return "Respuesta: " + self.text[:10] # first 10 characters of answer
    
    class Meta:
        verbose_name = "Texto de respuesta"
        verbose_name_plural = "Textos de respuesta"

class AnswerRating(models.Model):
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Rating")

    def __str__(self):
        return "Valuación: " + self.rating
    
    class Meta:
        verbose_name = "Valuación"
        verbose_name_plural = "Valuaciones"


"""An answer can be of 3 types and can only be one at the same time. Other Foreign Keys are in this case NULL. Answer-FK are initialized with NULL and not required"""
class Answer(models.Model):

    ANSWER_TYPES = [
        ('U', 'Carga'), # Upload
        ('T', 'Texto'), # Text
        ('R', 'Valuación'), # Rating
    ]

    type = models.CharField(max_length=1, choices=ANSWER_TYPES, verbose_name="Tipo")
    upload_answer = models.ForeignKey(AnswerUpload, on_delete=models.CASCADE, verbose_name="Carga", null=True, blank=True)
    text_answer = models.ForeignKey(AnswerText, on_delete=models.CASCADE, verbose_name="Texto", null=True, blank=True)
    rating_answer = models.ForeignKey(AnswerRating, on_delete=models.CASCADE, verbose_name="Valuación", null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name="Usuario") # Has to be user for easier implementation
    exercise = models.ForeignKey(ExerciseStep, on_delete=models.CASCADE, verbose_name="Ejercicio")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name="Actividad")
    submitted = models.DateTimeField(auto_now=True, verbose_name="Fecha de envío")

    def __str__(self):
        return "Tipo de respuesta: " + self.type + ", Estudiante: " + self.user.name + " " + self.user.first_lastname + " " + self.user.second_lastname
    
    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"
        ordering = ["submitted"]
        