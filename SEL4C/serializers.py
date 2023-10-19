from SEL4C.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_str
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


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
    
# Will raise ValidationError if the password is not matching requirements
    def validate_password(self, value):
        validate_password(value)  
        return value

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

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        username = user_data.get('email')

        existing_user = User.objects.filter(username=username).first()
        if existing_user:
            raise serializers.ValidationError("User with this email already exists.")

        # Create a User object
        user_serializer = UserRegistrationSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
        else:
            raise serializers.ValidationError(user_serializer.errors)

        student = Student.objects.create(
            user=user,
            age=validated_data.get('age'),
            agreed_policies=validated_data.get('agreed_policies'),
            gender=validated_data.get('gender'),
            country=validated_data.get('country'),
            studies=validated_data.get('studies'))

        if not student:
            user.delete() # Delete user if student couldnt be created
            raise serializers.ValidationError("Student could not be created")

        return student


"""Multi-use answer_string field. Depending on answer type gets interpreted in a different way, eg. as Int when Type=R (rating)"""
class AnswerSerializer(serializers.ModelSerializer):
    answer_string = serializers.CharField(style={"input_type": "text"}, write_only=True)

    activity = CreatableSlugRelatedField(
        many=False,
        slug_field='activity_number',
        queryset=Activity.objects.all()
    )

    exerciseStep = CreatableSlugRelatedField(
        many=False,
        slug_field='exerciseStep_number',
        queryset=ExerciseStep.objects.all()
    )
    class Meta:
        model = Answer
        fields = ["type", "answer_string", "activity", "exerciseStep"]

    def save(self, **kwargs):
        answer_type = self.validated_data['type']
        exerciseStep = self.validated_data['exerciseStep']
        activity = self.validated_data['activity']
        user = self.context['request'].user
        answer = Answer(type=answer_type, user=user, exercise=exerciseStep, activity=activity)

        match answer_type:
            case 'U':
                raise serializers.ValidationError({'type': 'Upload via /upload/'})
            
            case 'T':
                textAnswer = AnswerText(text=self.validated_data['answer_string'])
                textAnswer.save()
                answer.text_answer = textAnswer
                answer.save()


            case 'R':
                ratingAnswer = AnswerRating(rating=self.validated_data['answer_string'])
                ratingAnswer.save()
                answer.rating_answer = ratingAnswer
                answer.save()
                
            case _:
                raise serializers.ValidationError({'type': 'Type not defined'})

        return answer



class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    activity = CreatableSlugRelatedField(
        many=False,
        slug_field='activity_number',
        queryset=Activity.objects.all()
    )

    exerciseStep = CreatableSlugRelatedField(
        many=False,
        slug_field='exerciseStep_number',
        queryset=ExerciseStep.objects.all()
    )
