from django.shortcuts import render
from .serializers import UserSerializer,LoginUserSerializer,CsvUploadSerializer,SaveCsvSerializer,DiagnosisCodesSerializer
from rest_framework import viewsets, permissions
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import io, csv, pandas as pd
# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    queryset = ''
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


    def register(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response({"status":"User added succesfully"})
        else:
            return Response({"Fail": "blablal"}, status=status.HTTP_400_BAD_REQUEST)

class LoginUserViewSet(viewsets.ModelViewSet):
    queryset = ''
    serializer_class = LoginUserSerializer
    permission_classes = (permissions.AllowAny,)

    def login(self,request,format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validate_data
            status_code =status.HTTP_200_OK
            message="happpppy"
            return Response(status=status_code,message=message)

class CsvuploadViewSet(viewsets.ModelViewSet):
    serializer_class =  CsvUploadSerializer
    queryset = ''

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            file = serializer.validated_data['file']
            reader = pd.read_csv(file)
            for _, row in reader.iterrows():
                csv = File(
                    id = row['id'],
                    category_code = row['category_code'],
                    code_id = row['code_id'],
                    summary = row['summary'],
                    description= row['description'],
                    category_title  = row['category_title '],
                    icd_code= row['icd_code'],)

                csv.save()
                import pdb; pdb.set_trace() 
            return Response({"status":"CSV succesfully upload"})
            

class DiagnosisCodesViewSet(viewsets.ModelViewSet):
    queryset = ''
    serializer_class = DiagnosisCodesSerializer

    def createDiagnosis(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Fail": "yeeetetette"}, status=status.HTTP_201_CREATED)


    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)