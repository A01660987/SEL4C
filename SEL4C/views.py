from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from SEL4C.serializers import *
from SEL4C.models import *
from SEL4C.permissions import *


@extend_schema_view(
    list=extend_schema(description="Get a list"),
    retrieve=extend_schema(description="Get an item"),
    create=extend_schema(description="Create an item"),
    update=extend_schema(description="Update an item"),
    destroy=extend_schema(description="Delete an item"),
)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    get_permissions = permission_user

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    # TODO


class InstitutionViewSet(viewsets.ModelViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()
    get_permissions = permission_get


class DegreeViewSet(viewsets.ModelViewSet):
    serializer_class = DegreeSerializer
    queryset = Degree.objects.all()
    get_permissions = permission_get

class DisciplineViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplineSerializer
    queryset = Discipline.objects.all()
    get_permissions = permission_get


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    # TODO


class DiagnosisQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = DiagnosisQuestionSerializer
    queryset = DiagnosisQuestion.objects.all()
    get_permissions = permission_get


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    get_permissions = permission_get


class ImplementationProcessViewSet(viewsets.ModelViewSet):
    serializer_class = ImplementationProcessSerializer
    queryset = ImplementationProcess.objects.all()
    get_permissions = permission_get


class CompetenceDiagnosisViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenceDiagnosisSerializer
    queryset = CompetenceDiagnosis.objects.all()
    get_permissions = permission_get


class DiagnosisTestViewSet(viewsets.ModelViewSet):
    serializer_class = DiagnosisTestSerializer
    queryset = DiagnosisTest.objects.all()
    get_permissions = permission_get


class CompetenceViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenceSerializer
    queryset = Competence.objects.all()
    get_permissions = permission_get


class ResourceViewSet(viewsets.ModelViewSet):
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()
    get_permissions = permission_get


class TrainingReagentViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingReagentSerializer
    queryset = TrainingReagent.objects.all()
    get_permissions = permission_get


class TrainingActivityViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingActivitySerializer
    queryset = TrainingActivity.objects.all()
    get_permissions = permission_get
