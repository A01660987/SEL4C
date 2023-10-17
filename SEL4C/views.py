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

    def post(self, request, format=None):
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


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    #TODO what other views are necessary?



"""Creates an Answer object and UploadAnswer object automatically and stores the file in a user- and exercise specific directory"""
class FileUploadView(APIView):
    # parser_classes = (FileUploadParser,)
    parser_classes = (MultiPartParser,)
    serializer_class = FileUploadSerializer
    permission_classes = [FileUploadPermission]

    @csrf_exempt
    def post(self, request):
        if request.method == "POST" and request.FILES["file"] and request.user:

            file_serializer = FileUploadSerializer(data=request.data)
            if file_serializer.is_valid():
                activity = file_serializer.validated_data['activity']
                exerciseStep = file_serializer.validated_data['exerciseStep']
                user = request.user
                uploaded_file = request.FILES["file"]
                fs = FileSystemStorage()
            
                path = os.path.join(fs.location, user.username, str(activity.activity_number), str(exerciseStep.exerciseStep_number), uploaded_file.name)
                
                filename = fs.save(path, uploaded_file)
                uploaded_file_url = fs.url(filename)

                uploadAnswer = AnswerUpload(link=uploaded_file_url, filename=uploaded_file.name)
                uploadAnswer.save()
                answer = Answer(type='U', exercise=exerciseStep, activity=activity, user=user, upload_answer=uploadAnswer)
                answer.save()

                return JsonResponse({"status": "success"}, safe=False, status=201)
            
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({"status": "only 'POST' allowed"}, safe=False, status=404)
