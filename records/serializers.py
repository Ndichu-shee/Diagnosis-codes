from rest_framework import serializers
from rest_framework.serializers import FileField,Serializer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import DiagnosisCodes
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password','email')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'],is_staff=True )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginUserSerializer(serializers.Serializer):
    email= serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def post(self, validated_data):
        return User.objects.create(**validated_data)



class DiagnosisCodesSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiagnosisCodes
        fields = '__all__'  
             
class CsvUploadSerializer(serializers.Serializer):
    file = serializers.FileField()



