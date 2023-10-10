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

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Grupo")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        ordering = ["name"]

class Institution(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Institución")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
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
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, verbose_name="Grupo")
    degree = models.ManyToManyField(Degree, verbose_name="Título académico")

    REQUIRED_FIELDS = [
        'age',
        'agreed_policies',
    ]

    def __str__(self):
        return self.id.name + " " + self.id.first_lastname + " " + self.id.second_lastname

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ["user"]

class DiagnosisQuestion(models.Model):
    identificator = models.SmallAutoField(primary_key=True, null=False, editable=False, verbose_name="ID", unique=True)
    question = models.TextField(primary_key=False, null=False, editable=True, verbose_name="Question", unique=True)
    registered = models.DateTimeField(primary_key=False, null=False, editable=False, verbose_name="Registered", unique=False, auto_now_add=True)
    updated = models.DateTimeField(primary_key=False, null=False, editable=True, verbose_name="Updated", unique=False, auto_now_add=True)
    status = models.BooleanField(primary_key=False, null=False, editable=True, verbose_name="Status", unique=False, default=True)

    def __str__(self):
        return self.question
    
    class Meta:
        db_table = "diagnosisquestion"
        verbose_name = "Diagnosis Question"
        verbose_name_plural = "Diagnosis Questions"
        ordering = ["identificator"]

class Test(models.Model):
    identificator = models.SmallAutoField(primary_key=True, null=False, editable=False, verbose_name="ID", unique=True)
    denomination = models.CharField(primary_key=False, null=False, editable=True, verbose_name="Test", unique=True, max_length=25)
    description = models.CharField(primary_key=False, null=True, editable=True, verbose_name="Description", unique=False, max_length=50)
    status = models.BooleanField(primary_key=False, null=False, editable=True, verbose_name="Status", unique=False, default=True)
    diagnosisQuestions = models.ManyToManyField(DiagnosisQuestion)

    def __str__(self):
        return self.denomination
    
    class Meta:
        db_table = "test"
        verbose_name = "Test"
        verbose_name_plural = "Tests"
        ordering = ["identificator"]

class ImplementationProcess(models.Model):
    identificator = models.BigAutoField(primary_key=True, null=False, editable=False, verbose_name="ID", unique=True)
    registered = models.DateTimeField(primary_key=False, null=False, editable=False, verbose_name="Registered", unique=False, auto_now_add=True)
    updated = models.DateTimeField(primary_key=False, null=False, editable=True, verbose_name="Updated", unique=False, auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, primary_key=False, null=False, blank=False, editable=False, verbose_name="Student", unique=False)

    def __str__(self):
        return self.identificator
    
    class Meta:
        db_table = "implementationprocess"
        verbose_name = "Implementation Process"
        verbose_name_plural = "Implementation Processes"
        ordering = ["identificator"]

class CompetenceDiagnosis(models.Model):
    identificator = models.BigAutoField(primary_key=True, null=False, editable=False, verbose_name="ID", unique=True)
    completed = models.BooleanField(primary_key=False, null=False, editable=True, verbose_name="Completed", unique=False, default=True)
    registered = models.DateTimeField(primary_key=False, null=False, editable=False, verbose_name="Registered", unique=False, auto_now_add=True)
    implementationProcess = models.ForeignKey(ImplementationProcess, on_delete=models.CASCADE, primary_key=False, null=False, blank=False, editable=False, verbose_name="Implementation Process", unique=False)

    def __str__(self):
        return self.identificator
    
    class Meta:
        db_table = "competencediagnosis"
        verbose_name = "Competence Diagnosis"
        verbose_name_plural = "Competence Diagnoses"
        ordering = ["identificator"]

class DiagnosisTest(models.Model):
    identificator = models.BigAutoField(primary_key=True, null=False, editable=False, verbose_name="ID", unique=True)
    competenceDiagnosis = models.ForeignKey(CompetenceDiagnosis, on_delete=models.CASCADE, primary_key=False, null=False, blank=False, editable=False, verbose_name="Competence Diagnosis", unique=False)
    diagnosisQuestion = models.ForeignKey(DiagnosisQuestion, on_delete=models.CASCADE, primary_key=False, null=False, blank=False, editable=False, verbose_name="Diagnosis Question", unique=False)
    answer = models.PositiveSmallIntegerField(primary_key=False, null=False, editable=True, verbose_name="Answer", unique=False, validators=[MinValueValidator(0), MaxValueValidator(4)])

    def __str__(self):
        return self.identificator
    
    class Meta:
        db_table = "diagnosistest"
        verbose_name = "Diagnosis Test"
        verbose_name_plural = "DiagnosisTests"
        ordering = ["identificator"]
        unique_together = (("competenceDiagnosis", "diagnosisQuestion"), )

class Competence(models.Model):
    identificator = models.SmallAutoField(primary_key=True, null=False, editable=False, verbose_name="ID", unique=True)
    denomination = models.CharField(primary_key=False, null=False, editable=True, verbose_name="Competence", unique=True, max_length=50)
    description = models.TextField(primary_key=False, null=True, editable=True, verbose_name="Description", unique=False)
    registered = models.DateTimeField(primary_key=False, null=False, editable=False, verbose_name="Registered", unique=False, auto_now_add=True)
    updated = models.DateTimeField(primary_key=False, null=False, editable=True, verbose_name="Updated", unique=False, auto_now_add=True)
    status = models.BooleanField(primary_key=False, null=False, editable=True, verbose_name="Status", unique=False, default=True)

    def __str__(self):
        return self.denomination
    
    class Meta:
        db_table = "competence"
        verbose_name = "Competence"
        verbose_name_plural = "Competences"
        ordering = ["identificator"]

class Resource(models.Model):
    identificator = models.SmallAutoField(primary_key=True, null=False, editable=False, verbose_name="ID", unique=True)
    denomination = models.CharField(primary_key=False, null=False, editable=True, verbose_name="Resource", unique=True, max_length=25)
    link = models.TextField(primary_key=False, null=False, editable=True, verbose_name="Link", unique=True)
    description = models.TextField(primary_key=False, null=True, editable=True, verbose_name="Description", unique=False)
    registered = models.DateTimeField(primary_key=False, null=False, editable=False, verbose_name="Registered", unique=False, auto_now_add=True)
    updated = models.DateTimeField(primary_key=False, null=False, editable=True, verbose_name="Updated", unique=False, auto_now_add=True)
    status = models.BooleanField(primary_key=False, null=False, editable=True, verbose_name="Status", unique=False, default=True)

    def __str__(self):
        return self.denomination
    
    class Meta:
        db_table = "resource"
        verbose_name = "Resource"
        verbose_name_plural = "Resources"
        ordering = ["identificator"]

class TrainingReagent(models.Model):
    identificator = models.SmallAutoField(primary_key=True, null=False, editable=False, verbose_name="ID", unique=True)
    denomination = models.CharField(primary_key=False, null=False, editable=True, verbose_name="Training Reagent", unique=True, max_length=50)
    goals = models.TextField(primary_key=False, null=True, editable=True, verbose_name="Goals", unique=False)
    description = models.TextField(primary_key=False, null=True, editable=True, verbose_name="Description", unique=False)
    indications = models.TextField(primary_key=False, null=True, editable=True, verbose_name="Indications", unique=False)
    questions = models.TextField(primary_key=False, null=True, editable=True, verbose_name="Questions", unique=False)
    registered = models.DateTimeField(primary_key=False, null=False, editable=False, verbose_name="Registered", unique=False, auto_now_add=True)
    updated = models.DateTimeField(primary_key=False, null=False, editable=True, verbose_name="Updated", unique=False, auto_now_add=True)
    status = models.BooleanField(primary_key=False, null=False, editable=True, verbose_name="Status", unique=False, default=True)
    competences = models.ManyToManyField(Competence)
    resources = models.ManyToManyField(Resource)

    def __str__(self):
        return self.denomination
    
    class Meta:
        db_table = "trainingreagent"
        verbose_name = "Training Reagent"
        verbose_name_plural = "Training Reagents"
        ordering = ["identificator"]

class TrainingActivity(models.Model):
    identificator = models.BigAutoField(primary_key=True, null=False, editable=False, verbose_name="ID", unique=True)
    trainingReagent = models.ForeignKey(TrainingReagent, on_delete=models.CASCADE, primary_key=False, null=False, blank=False, editable=False, verbose_name="Training Reagent", unique=False)
    implementationProcess = models.ForeignKey(ImplementationProcess, on_delete=models.CASCADE, primary_key=False, null=False, blank=False, editable=False, verbose_name="Implementation Process", unique=False)
    link = models.TextField(primary_key=False, null=True, editable=False, verbose_name="Link", unique=False)
    completed = models.BooleanField(primary_key=False, null=False, editable=True, verbose_name="Completed", unique=False, default=True)
    registered = models.DateTimeField(primary_key=False, null=False, editable=False, verbose_name="Registered", unique=False, auto_now_add=True)

    def __str__(self):
        return self.identificator
    
    class Meta:
        db_table = "trainingactivity"
        verbose_name = "Training Activity"
        verbose_name_plural = "Training Activities"
        ordering = ["identificator"]
        unique_together = (("trainingReagent", "implementationProcess"), )
