from django.shortcuts import render
from .serializers import UserSerializer,LoginUserSerializer,CsvUploadSerializer,SaveCsvSerializer,DiagnosisCodesSerializer
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import DiagnosisCodes
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import pandas as pd
from diagnosis_codes.settings import EMAIL_HOST_USER
from django.core import mail
from django.core.mail import send_mail
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class UserView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class LoginUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to login
    """
    queryset = ''
    serializer_class = LoginUserSerializer
    permission_classes = (permissions.AllowAny,)

    def login(self,request,format=None):
        serializer = self.serializer_class(data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validate_data
            return Response(status=status.HTTP_200_OK) 

class CsvuploadView(generics.CreateAPIView):
    """
    API endpoint that allows logged in users to upload a csv and receive an email after uploading
    """
    serializer_class =  CsvUploadSerializer
    permission_classes = (IsAuthenticated,)


  
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            file = serializer.validated_data['file']
            reader = pd.read_csv(file)
            print(reader)
            for _, row in reader.iterrows():
                DiagnosisCodes.objects.create(
               
                    category_code  = row['category_code'],
                    code_id = row['code_id'],
                    addition_code  = row['addition_code'],
                    summary= row['summary'],
                    description= row['description'],
                    category_title  = row['category_title'],

                    )
                
            emails=request.user.email
            subject = "mPharma CSV upload"
            message = "Your CSV was successfully uploaded"
            recipient=emails
            send_mail(subject, message,EMAIL_HOST_USER,[recipient])  
                

                # import pdb; pdb.set_trace() 
            return Response({"status":"CSV succesfully uploaded"})
            

class DiagnosisCodesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to create a new diagnosis code, list all the codes, get by id, update a specific record and delete a record
    """
    queryset = DiagnosisCodes.objects.all()
    serializer_class = DiagnosisCodesSerializer

   

    