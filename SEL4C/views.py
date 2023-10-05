from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from .serializers import *
from .models import *
from .permissions import *


@extend_schema_view(
    list=extend_schema(description="Get a list"),
    retrieve=extend_schema(description="Get an item"),
    create=extend_schema(description="Create an item"),
    update=extend_schema(description="Update an item"),
    destroy=extend_schema(description="Delete an item"),
)
# class GenderViewSet(viewsets.ModelViewSet):
#     serializer_class = GenderSerializer
#     queryset = Gender.objects.all()
#     permission_classes = [only_get_for_authenticated_users]


# class CountryViewSet(viewsets.ModelViewSet):
#     serializer_class = CountrySerializer
#     queryset = Country.objects.all()
#     permission_classes = [only_get_for_authenticated_users]


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [user_permissions]


class AdministratorViewSet(viewsets.ModelViewSet):
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()
    # TODO


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    # TODO


class InstitutionViewSet(viewsets.ModelViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()
    permission_classes = [list_authenticated]


class AcademicDegreeViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicDegreeSerializer
    queryset = AcademicDegree.objects.all()
    permission_classes = [list_authenticated]


class AcademicDegreeOfferViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicDegreeOfferSerializer
    queryset = AcademicDegreeOffer.objects.all()
    permission_classes = [list_authenticated]


class AcademicDisciplineViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicDisciplineSerializer
    queryset = AcademicDiscipline.objects.all()
    permission_classes = [list_authenticated]


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    # TODO


class DiagnosisQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = DiagnosisQuestionSerializer
    queryset = DiagnosisQuestion.objects.all()
    permission_classes = [list_authenticated]


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = [list_authenticated]


class ImplementationProcessViewSet(viewsets.ModelViewSet):
    serializer_class = ImplementationProcessSerializer
    queryset = ImplementationProcess.objects.all()
    permission_classes = [list_authenticated]


class CompetenceDiagnosisViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenceDiagnosisSerializer
    queryset = CompetenceDiagnosis.objects.all()
    permission_classes = [list_authenticated]


class DiagnosisTestViewSet(viewsets.ModelViewSet):
    serializer_class = DiagnosisTestSerializer
    queryset = DiagnosisTest.objects.all()
    permission_classes = [list_authenticated]


class CompetenceViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenceSerializer
    queryset = Competence.objects.all()
    permission_classes = [list_authenticated]


class ResourceViewSet(viewsets.ModelViewSet):
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()
    permission_classes = [list_authenticated]


class TrainingReagentViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingReagentSerializer
    queryset = TrainingReagent.objects.all()
    permission_classes = [list_authenticated]


class TrainingActivityViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingActivitySerializer
    queryset = TrainingActivity.objects.all()
    permission_classes = [list_authenticated]
