from SEL4C.models import User, Group, Institution, Discipline, Degree, Student, DiagnosisQuestion, Test, ImplementationProcess, CompetenceDiagnosis, DiagnosisTest, Competence, Resource, TrainingReagent, TrainingActivity
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_str
from rest_framework import serializers


"""Difference between SlugRelatedField is the creation of an object if no object is found"""
class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_str(data))
        except (TypeError, ValueError):
            self.fail('invalid')

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "password2", "name", "first_lastname", "second_lastname"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        name = self.validated_data['name'] 
        first_lastname = self.validated_data['first_lastname'] 
        second_lastname = self.validated_data['second_lastname']

        user = User(username=email, name=name, first_lastname=first_lastname, second_lastname=second_lastname, **kwargs)

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
    
# TODO   
# class PasswordChangeSerializer(serializers.Serializer):
#     current_password = serializers.CharField(style={"input_type": "password"}, required=True)
#     new_password = serializers.CharField(style={"input_type": "password"}, required=True)

#     def validate_current_password(self, value):
#         if not self.context['request'].user.check_password(value):
#             raise serializers.ValidationError({'current_password': 'Does not match'})
#         return value

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields="__all__"

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institution
        fields="__all__"

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Degree
        fields="__all__"

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Discipline
        fields="__all__"

class StudentSerializer(serializers.ModelSerializer):

    user = UserRegistrationSerializer()
    class Meta:
        model=Student
        fields="__all__"

    group = CreatableSlugRelatedField(
        many=False,
        slug_field='id',
        queryset=Group.objects.all()
    )
    Disciplines = CreatableSlugRelatedField(
        many=True,
        slug_field='id',
        queryset=Discipline.objects.all()
    )



class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()