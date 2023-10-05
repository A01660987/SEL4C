from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from django.http import JsonResponse
from SEL4C.serializers import GenderSerializer, CountrySerializer, UserSerializer, AdministratorSerializer, GroupSerializer, InstitutionSerializer, AcademicDegreeSerializer, AcademicDegreeOfferSerializer, AcademicDisciplineSerializer, StudentSerializer, DiagnosisQuestionSerializer, TestSerializer, ImplementationProcessSerializer, CompetenceDiagnosisSerializer, DiagnosisTestSerializer, CompetenceSerializer, ResourceSerializer, TrainingReagentSerializer, TrainingActivitySerializer
from SEL4C.models import Gender, Country, User, Administrator, Group, Institution, AcademicDegree, AcademicDegreeOffer, AcademicDiscipline, Student, DiagnosisQuestion, Test, ImplementationProcess, CompetenceDiagnosis, DiagnosisTest, Competence, Resource, TrainingReagent, TrainingActivity
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
from querystring_parser import parser

@extend_schema_view(
    list=extend_schema(description="Get a list"), 
    retrieve=extend_schema(description="Get an item"), 
    create=extend_schema(description="Create an item"), 
    update=extend_schema(description="Update an item"), 
    destroy=extend_schema(description="Delete an item"),
)

class GenderViewSet(viewsets.ModelViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class AdministratorViewSet(viewsets.ModelViewSet):
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class InstitutionViewSet(viewsets.ModelViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()

class AcademicDegreeViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicDegreeSerializer
    queryset = AcademicDegree.objects.all()

class AcademicDegreeOfferViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicDegreeOfferSerializer
    queryset = AcademicDegreeOffer.objects.all()

class AcademicDisciplineViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicDisciplineSerializer
    queryset = AcademicDiscipline.objects.all()

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class DiagnosisQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = DiagnosisQuestionSerializer
    queryset = DiagnosisQuestion.objects.all()

class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

class ImplementationProcessViewSet(viewsets.ModelViewSet):
    serializer_class = ImplementationProcessSerializer
    queryset = ImplementationProcess.objects.all()

class CompetenceDiagnosisViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenceDiagnosisSerializer
    queryset = CompetenceDiagnosis.objects.all()

class DiagnosisTestViewSet(viewsets.ModelViewSet):
    serializer_class = DiagnosisTestSerializer
    queryset = DiagnosisTest.objects.all()

class CompetenceViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenceSerializer
    queryset = Competence.objects.all()

class ResourceViewSet(viewsets.ModelViewSet):
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()

class TrainingReagentViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingReagentSerializer
    queryset = TrainingReagent.objects.all()

class TrainingActivityViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingActivitySerializer
    queryset = TrainingActivity.objects.all()

@csrf_exempt
def activity(request):
    match request.method:
        case "GET":
            queryset=TrainingReagent.objects.select_related("competences", "resources").filter(identificator=int(json.loads(request.body)["identificator"])).values("identificator", "denomination", "goals", "description", "indications", "questions")
            if queryset:
                queryset = list(queryset)[0]
                queryset["goals"] = queryset["goals"].split("\u0000") if queryset["goals"] else None
                queryset["description"] = queryset["description"].split("\u0000") if queryset["description"] else None
                queryset["indications"] = queryset["indications"].split("\u0000") if queryset["indications"] else None
                queryset["questions"] = queryset["questions"].split("\u0000") if queryset["questions"] else None
                return JsonResponse(queryset, safe=False, status=200)
            else:
                return JsonResponse({"mensaje": "no"}, safe=False, status=404)
        case "POST":
            data = "{\"identificator\": 1,\"activity\": 2,\"content\": [{\"screen\": 1,\"content\": \"string\",\"media\": null}]}"
            response = json.loads(data)
            return JsonResponse(response, safe=False, status=202)
        case _:
            return JsonResponse({"mensaje": "no"}, safe=False, status=404)

@csrf_exempt
def diagnosis(request):
    match request.method:
        case "GET":
            tests=Test.objects.filter(Q(denomination = "Perfil del Emprendedor Social") | Q(denomination = "Pensamiento Complejo"))
            if tests:
                questions = []
                for index in range(len(tests)):
                    questions.append(list(tests[index].diagnosisQuestions.all().values("identificator", "question")))
                queryset = tests.values("identificator", "denomination", "description")
                queryset = list(queryset)
                for index in range(len(questions)):
                    queryset[index]["diagnosisQuestions"] = questions[index]
                return JsonResponse(queryset, safe=False, status=200)
        case "POST":
            data = "{\"identificator\": 1,\"activity\": 2,\"content\": [{\"screen\": 1,\"content\": \"string\",\"media\": null}]}"
            response = json.loads(data)
            return JsonResponse(response, safe=False, status=202)
        case _:
            return JsonResponse({"mensaje": "no"}, safe=False, status=404)

@csrf_exempt
def credentials(request):
    match request.method:
        case "GET":
            #response = parser.parse(request.body)
            print(request.body)
            correo="claudia@utez.edu.mx"
            contra="bcrypt_sha256$$2b$12$qCOpcRe.nJPC/NK6vST6r.ZeAYUhsNHttXw2yqASygDq91cTo8GkS"
            user=User.objects.filter(email=correo, password=contra)[0]
            if user:
                student = Student.objects.get(identificator = user)
                implementationProcess = ImplementationProcess.objects.get(student = student)
                return JsonResponse({"implementationProcess": implementationProcess.identificator}, safe=False, status=200)
            else:
                return JsonResponse({"mensaje": "no"}, safe=False, status=404)
        case "POST":
            response = parser.parse(request.body)
            print(response)
            user = User.objects.create(gender=Gender.objects.get(identificator=1), country=Country.objects.get(identificator=20), email="claudia@utez.edu.mx", name="Claudia", firstLastname="Vivas", secondLastname=None, age=17, password="123", agreedPolicies=True)
            student = Student.objects.create(identificator = user, group=Group.objects.get(identificator=1), code="S"+str(user.identificator))
            student.academicDisciplines.add(AcademicDiscipline.objects.get(identificator = 1))
            implementationProcess = ImplementationProcess.objects.create(student=student)
            return JsonResponse({"implementationProcess": implementationProcess.identificator}, safe=False, status=202)
        case _:
            return JsonResponse({"mensaje": "no"}, safe=False, status=404)
