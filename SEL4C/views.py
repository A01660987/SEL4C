from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.response import Response
from SEL4C.serializers import *
from SEL4C.models import *
from django.views.decorators.csrf import csrf_exempt
import os
from django.core.files.storage import FileSystemStorage
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from .permissions import *
from rest_framework import status
from django.contrib.auth import update_session_auth_hash


@extend_schema_view(
    list=extend_schema(description="Get a list"), 
    retrieve=extend_schema(description="Get an item"), 
    create=extend_schema(description="Create an item"), 
    update=extend_schema(description="Update an item"), 
    destroy=extend_schema(description="Delete an item"),
)

# class UserViewSet(viewsets.GenericViewSet):
#     serializer_class = UserRegistrationSerializer
#     queryset = User.objects.all()
#     permission_classes = [CustomUserPermission]

#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get_queryset(self):

#         user = self.request.user
#         # Return own user object back
#         if user.is_authenticated:
#             return User.objects.filter(pk=user.pk)
        
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
            


class StudentViewSet(viewsets.GenericViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [CustomUserPermission]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user
        # Return own student object back
        if user.is_authenticated:
            return Student.objects.filter(user=user.pk)
        
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ChangeEmailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangeEmailSerializer

    def post(self, request):
        serializer = ChangeEmailSerializer(data=request.data)
        if serializer.is_valid():
            new_email = serializer.validated_data['email']
            user = request.user
            user.username = new_email
            user.save()
            return Response({'message': 'Email changed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            new_password = serializer.validated_data['password']
            user = request.user
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Important to maintain the session
            return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""Get a list of all Institutions available"""
class InstitutionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()
    permission_classes = [permissions.AllowAny]


"""Get a list of available degrees in an institution"""
class DegreeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DegreeSerializer
    queryset = Degree.objects.all()
    permission_classes = [permissions.AllowAny]


    def get_queryset(self):
        institution_id = self.request.query_params.get('institution_id')

        # If id provided, return objects which are available for this institution
        if institution_id:
            return Degree.objects.filter(availablestudies__institution_id=institution_id).distinct()
        else:
            # Return the original queryset if institution_id is not provided
            return self.queryset


"""Get a list of available disciplines with according Institution and degree id"""
class DisciplineViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DisciplineSerializer
    queryset = Discipline.objects.all()
    permission_classes = [permissions.AllowAny]


    def get_queryset(self):
        institution_id = self.request.query_params.get('institution_id')
        degree_id = self.request.query_params.get('degree_id')

        # If id provided, return objects which are available for this institution
        if institution_id:
            return Discipline.objects.filter(availablestudies__institution_id=institution_id,
                                         availablestudies__degree_id=degree_id
                                         )
        else:
            # Return the original queryset if institution_id is not provided
            return self.queryset



class AnswerViewSet(APIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    @csrf_exempt
    def post(self, request):
        if request.method == "POST" and request.user:
            answer_serializer = AnswerSerializer(data=request.data)
            if answer_serializer.is_valid():
                answer_serializer.save()
                return JsonResponse({"status": "success"}, safe=False, status=201)
            
            return Response(answer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return JsonResponse({"status": "only 'POST' allowed"}, safe=False, status=404)
    #TODO what other views (POST, etc) are necessary?



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
