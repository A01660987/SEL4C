from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from SEL4C.serializers import GenderSerializer, CountrySerializer, UserSerializer, AdministratorSerializer, GroupSerializer, InstitutionSerializer, AcademicDegreeSerializer, AcademicDegreeOfferSerializer, AcademicDisciplineSerializer, StudentSerializer, DiagnosisQuestionSerializer, TestSerializer, ImplementationProcessSerializer, CompetenceDiagnosisSerializer, DiagnosisTestSerializer, CompetenceSerializer, ResourceSerializer, TrainingReagentSerializer, TrainingActivitySerializer
from SEL4C.models import Gender, Country, User, Administrator, Group, Institution, AcademicDegree, AcademicDegreeOffer, AcademicDiscipline, Student, DiagnosisQuestion, Test, ImplementationProcess, CompetenceDiagnosis, DiagnosisTest, Competence, Resource, TrainingReagent, TrainingActivity

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
