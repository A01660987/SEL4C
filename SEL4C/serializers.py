from SEL4C.models import Gender, Country, User, Administrator, Group, Institution, AcademicDegree, AcademicDegreeOffer, AcademicDiscipline, Student, DiagnosisQuestion, Test, ImplementationProcess, CompetenceDiagnosis, DiagnosisTest, Competence, Resource, TrainingReagent, TrainingActivity
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_str
from rest_framework import serializers

class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_str(data))
        except (TypeError, ValueError):
            self.fail('invalid')

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Gender
        fields="__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    gender = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=Gender.objects.all()
    )
    country = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=Country.objects.all()
    )
    class Meta:
        model=User
        fields="__all__"

class AdministratorSerializer(serializers.ModelSerializer):
    identificator = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=User.objects.all()
    )
    class Meta:
        model=Administrator
        fields="__all__"

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields="__all__"

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institution
        fields="__all__"

class AcademicDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model=AcademicDegree
        fields="__all__"

class AcademicDegreeOfferSerializer(serializers.ModelSerializer):
    institution = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=Institution.objects.all()
    )
    academicDegree = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=AcademicDegree.objects.all()
    )
    class Meta:
        model=AcademicDegreeOffer
        fields="__all__"

class AcademicDisciplineSerializer(serializers.ModelSerializer):
    academicDegreeOffer = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=AcademicDegreeOffer.objects.all()
    )
    class Meta:
        model=AcademicDiscipline
        fields="__all__"

class StudentSerializer(serializers.ModelSerializer):
    identificator = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=User.objects.all()
    )
    group = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=Group.objects.all()
    )
    academicDisciplines = CreatableSlugRelatedField(
        many=True,
        slug_field='identificator',
        queryset=AcademicDiscipline.objects.all()
    )
    class Meta:
        model=Student
        fields="__all__"

class DiagnosisQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=DiagnosisQuestion
        fields="__all__"

class TestSerializer(serializers.ModelSerializer):
    diagnosisQuestions = CreatableSlugRelatedField(
        many=True,
        slug_field='identificator',
        queryset=DiagnosisQuestion.objects.all()
    )
    class Meta:
        model=Test
        fields="__all__"

class ImplementationProcessSerializer(serializers.ModelSerializer):
    student = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=Student.objects.all()
    )
    class Meta:
        model=ImplementationProcess
        fields="__all__"

class CompetenceDiagnosisSerializer(serializers.ModelSerializer):
    implementationProcess = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=ImplementationProcess.objects.all()
    )
    class Meta:
        model=CompetenceDiagnosis
        fields="__all__"

class DiagnosisTestSerializer(serializers.ModelSerializer):
    competenceDiagnosis = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=CompetenceDiagnosis.objects.all()
    )
    diagnosisQuestion = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=DiagnosisQuestion.objects.all()
    )
    class Meta:
        model=DiagnosisTest
        fields="__all__"

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Competence
        fields="__all__"

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resource
        fields="__all__"

class TrainingReagentSerializer(serializers.ModelSerializer):
    competences = CreatableSlugRelatedField(
        many=True,
        slug_field='identificator',
        queryset=Competence.objects.all()
    )
    resources = CreatableSlugRelatedField(
        many=True,
        slug_field='identificator',
        queryset=Resource.objects.all()
    )
    class Meta:
        model=TrainingReagent
        fields="__all__"

class TrainingActivitySerializer(serializers.ModelSerializer):
    trainingReagent = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=TrainingReagent.objects.all()
    )
    implementationProcess = CreatableSlugRelatedField(
        many=False,
        slug_field='identificator',
        queryset=ImplementationProcess.objects.all()
    )
    class Meta:
        model=TrainingActivity
        fields="__all__"
