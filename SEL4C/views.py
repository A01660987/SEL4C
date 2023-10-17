from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.response import Response
from SEL4C.serializers import *
from SEL4C.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json, os
from querystring_parser import parser
from django.core.files.storage import FileSystemStorage
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from .permissions import *
from rest_framework import status


@extend_schema_view(
    list=extend_schema(description="Get a list"), 
    retrieve=extend_schema(description="Get an item"), 
    create=extend_schema(description="Create an item"), 
    update=extend_schema(description="Update an item"), 
    destroy=extend_schema(description="Delete an item"),
)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = [CustomUserPermission]
    #TODO allow creation for users but not with priviliges



class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class InstitutionViewSet(viewsets.ModelViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()

class DegreeViewSet(viewsets.ModelViewSet):
    serializer_class = DegreeSerializer
    queryset = Degree.objects.all()

class DisciplineViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplineSerializer
    queryset = Discipline.objects.all()

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [CustomUserPermission]
    #TODO allow creation for users but not with priviliges

    def post(self, request, format=None):
        # Deserialize the request data
        student_data = request.data

        # Extract user data from student data
        user_data = student_data.pop('user')

        # Create a User object
        user_serializer = UserRegistrationSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create a Student object associated with the User
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save(user=user)
            return Response(student_serializer.data, status=status.HTTP_201_CREATED)
        else:
            # If there is an error in the Student data, delete the User
            user.delete()
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





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
            else:
                return JsonResponse({"mensaje": "no"}, safe=False, status=404)
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
            user = User.objects.create(gender='F', country="MX", email="claudia@utez.edu.mx", name="Claudia", firstLastname="Vivas", secondLastname=None, age=17, password="123", agreedPolicies=True)
            student = Student.objects.create(identificator = user, group=Group.objects.get(identificator=1), code="S"+str(user.identificator))
            implementationProcess = ImplementationProcess.objects.create(student=student)
            return JsonResponse({"implementationProcess": implementationProcess.identificator}, safe=False, status=202)
        case _:
            return JsonResponse({"mensaje": "no"}, safe=False, status=404)


class FileUploadView(APIView):
    # parser_classes = (FileUploadParser,)
    parser_classes = (MultiPartParser,)
    serializer_class = FileUploadSerializer
    permission_classes = [FileUploadPermission]

    @csrf_exempt
    def post(self, request):
        if request.method == "POST" and request.FILES["file"] and request.user:

            serializer = FileUploadSerializer(data=request.data)
            if serializer.is_valid():
            # actividad = request.POST["activity"]
            # nombre_evidencia = request.POST["evidence_name"]
            #TODO add fields/folders for activity
                user = request.user
                uploaded_file = request.FILES["file"]
                fs = FileSystemStorage()
            
                path = os.path.join(fs.location, user.username, uploaded_file.name)
                
                filename = fs.save(path, uploaded_file)
                uploaded_file_url = fs.url(filename)

                return JsonResponse({"status": "success"}, safe=False, status=201)

        return JsonResponse({"status": "error"}, safe=False, status=404)
