from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.hashers import make_password

from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

class User(AbstractUser):
    username = None
    first_name = None
    last_name = None

    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    name = models.CharField(max_length=150, verbose_name="Nombre(s)")
    firstLastName = models.CharField(max_length=150, verbose_name="Apellido paterno")
    secondLastName = models.CharField(max_length=150, verbose_name="Apellido materno")
    dateRegistered = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    dateModified = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    status = models.BooleanField(default=True, verbose_name="Estatus")
    
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [
        'name',
        'firstLastName',
        'secondLastName',
        'dateRegistered',
        'dateModified',
        'status',
    ]

    def __str__(self):
        return self.email

class Student(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True, verbose_name="ID")
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(130)], verbose_name="Edad")
    agreedPolicies = models.BooleanField(default=True, verbose_name="¿Acepta las políticas de privacidad?")
    
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('N', 'No binario'),
        ('O', 'Otro'),
        ('P', 'Prefiero no decir'),
    ]
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country = CountryField()

class Admin(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True, verbose_name="ID")
    code = models.CharField(max_length=25, unique=True, verbose_name="Código")

    def __str__(self):
        return self.code

class Group(models.Model):
    denomination = models.CharField(max_length=25, unique=True, verbose_name="Grupo")
    description = models.CharField(max_length=50, verbose_name="Descripción")
    status = models.BooleanField(default=True, verbose_name="Estatus")

    def __str__(self):
        return self.denomination

class Institution(models.Model):
    identificator = models.SmallAutoField(primary_key=True, null=False, editable=False, verbose_name="ID", unique=True)
    denomination = models.CharField(primary_key=False, null=False, editable=True, verbose_name="Institution", unique=True, max_length=25)
    description = models.CharField(primary_key=False, null=True, editable=True, verbose_name="Description", unique=False, max_length=50)
    status = models.BooleanField(primary_key=False, null=False, editable=True, verbose_name="Status", unique=False, default=True)

    def __str__(self):
        return self.denomination
    
    class Meta:
        db_table = "institution"
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"
        ordering = ["identificator"]

class AcademicDegree(models.Model):
    identificator = models.SmallAutoField(primary_key=True, null=False, editable=False, verbose_name="ID", unique=True)
    denomination = models.CharField(primary_key=False, null=False, editable=True, verbose_name="Academic Degree", unique=True, max_length=25)
    status = models.BooleanField(primary_key=False, null=False, editable=True, verbose_name="Status", unique=False, default=True)

    def __str__(self):
        return self.denomination
    
    class Meta:
        db_table = "academicdegree"
        verbose_name = "Academic Degree"
        verbose_name_plural = "Academic Degrees"
        ordering = ["identificator"]

class AcademicDegreeOffer(models.Model):
    identificator = models.SmallAutoField(primary_key=True, null=False, editable=False, verbose_name="ID", unique=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, primary_key=False, null=False, blank=False, editable=False, verbose_name="Institution", unique=False)
    academicDegree = models.ForeignKey(AcademicDegree, on_delete=models.CASCADE, primary_key=False, null=False, blank=False, editable=False, verbose_name="Academic Degree", unique=False)
    denomination = models.CharField(primary_key=False, null=False, editable=True, verbose_name="Academic Degree Offer", unique=True, max_length=25)
    description = models.CharField(primary_key=False, null=True, editable=True, verbose_name="Description", unique=False, max_length=50)
    status = models.BooleanField(primary_key=False, null=False, editable=True, verbose_name="Status", unique=False, default=True)

    def __str__(self):
        return self.denomination
    
    class Meta:
        db_table = "academicdegreeoffer"
        verbose_name = "Academic Degree Offer"
        verbose_name_plural = "Academic Degree Offers"
        ordering = ["identificator"]

class AcademicDiscipline(models.Model):
    identificator = models.SmallAutoField(primary_key=True, null=False, editable=False, verbose_name="ID", unique=True)
    denomination = models.CharField(primary_key=False, null=False, editable=True, verbose_name="Academic Discipline", unique=False, max_length=25)
    description = models.CharField(primary_key=False, null=True, editable=True, verbose_name="Description", unique=False, max_length=50)
    status = models.BooleanField(primary_key=False, null=False, editable=True, verbose_name="Status", unique=False, default=True)
    academicDegreeOffer = models.ForeignKey(AcademicDegreeOffer, on_delete=models.CASCADE, primary_key=False, null=False, blank=False, editable=True, verbose_name="Academic Degree Offer", unique=False)

    def __str__(self):
        return self.denomination
    
    class Meta:
        db_table = "academicdiscipline"
        verbose_name = "Academic Discipline"
        verbose_name_plural = "Academic Disciplines"
        ordering = ["identificator"]

class Student(models.Model):
    identificator = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, null=False, blank=False, editable=False, verbose_name="ID", unique=True)
    code = models.CharField(primary_key=False, null=False, editable=True, verbose_name="Code", unique=True, max_length=25)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, primary_key=False, null=False, blank=False, editable=True, verbose_name="Group", unique=False)
    status = models.BooleanField(primary_key=False, null=False, editable=True, verbose_name="Status", unique=False, default=True)
    academicDisciplines = models.ManyToManyField(AcademicDiscipline)

    def __str__(self):
        return self.code
    
    class Meta:
        db_table = "student"
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ["identificator"]

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
