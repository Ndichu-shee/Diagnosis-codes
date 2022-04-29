from rest_framework import serializers
from rest_framework.serializers import FileField,Serializer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from  django.contrib.auth import authenticate
from .models import DiagnosisCodes

class  UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(min_length=6, write_only=True, required=True)
    password= serializers.CharField(min_length=6, write_only=True, required=True)

    class Meta:
        model = User 
        fields = ('id','username','email','password')
        extra_kwargs = {'password': {'write_only':True}}

    def post(self, validated_data):
        new_user = User.objects.create_user(validated_data['username'],None,validated_data['password'])
        return new_user

class LoginUserSerializer(serializers.Serializer):
    email= serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class DiagnosisCodesSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiagnosisCodes
        fields = '__all__'  
             
class CsvUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class SaveCsvSerializer(serializers.Serializer):
    class Meta:
        model = DiagnosisCodes
        fields = "__all__"


