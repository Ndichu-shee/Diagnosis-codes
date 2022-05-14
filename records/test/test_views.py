from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from records.models import *
from records.views import *

from rest_framework import status


class RegisterTest(APITestCase):
    
    def setUp(self):
        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.codes_list_url = reverse('diagnosis-codes-list')
        self.data=DiagnosisCodes.objects.create(
            category_code='A00',
            code_id='0' ,
            addition_code="A000",
            summary='Cholera due to Vibrio cholerae 01, biovar cholerae',
            description='Cholera due to Vibrio cholerae 01, biovar cholerae',
            category_title='Cholera', 
        )
    
        
    def test_create_user(self):
    
        data = {
            'username': 'joyce',
            'email':'joyce@gmail.com',
            'password':'wanjirundichu'
        }
        url = f"{'/create_user/'}"
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'],data['username'])

    def test_login_user(self):
        data = {
          
            'email':'joycee@gmail.com',
            'password':'wanjirundichu'
        }
        url = f"{'/login_user/'}"
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['email'],data['email'])

    # def test_ulpoad_csv(self):
    #     data = {
    #         'username': 'joyce',
    #         'password':'wanjirundichu'
    #     }
    #     file = SimpleUploadedFile("file.csv", b"abcdef", content_type="text/csv")
    #     data= {"file": file}
    #     response = self.client.post('/diagnosis-codes-upload/', data, format="multipart")
    #     self.assertEqual(response.status_code, 200)
    
    
    def test_create_record(self):
        data = {
            'category_code':'A00',
            'code_id':'0' ,
            'addition_code':"A000",
            'summary':'Cholera due to Vibrio cholerae 01, biovar cholerae',
            'description':'Cholera due to Vibrio cholerae 01, biovar cholerae',
            'category_title':'Cholera', 
        }
        response = self.client.post(self.codes_list_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_wrong_record(self):
        data = {
            'category_code':'A00',
            'code_id':'0' ,
            'addition_code':"A000",
            'summary':'Cholera due to Vibrio cholerae 01, biovar cholerae',
            'description':'Cholera due to Vibrio cholerae 01, biovar cholerae',
            'category_title':'',
        }
        response = self.client.post(self.codes_list_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)


    def test_get_codes_list(self):
        response = self.client.get(self.codes_list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_get_record_id(self):
      
        current_url = f'{self.codes_list_url}{self.data.id}/'
        response = self.client.get(current_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
  
    # def test_get_wrong_record_id(self):
    
    #     current_url = f'{self.codes_list_url}{self.data.id}/'
    #     response = self.client.get(current_url)
    #     self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    def test_update_record_id(self):
        update_data = {
            'category_code':'A00',
            'code_id':'0' ,
            'addition_code':"A000",
            'summary':'Cholera due to Vibrio cholerae 01, biovar cholerae',
            'description':'Cholera due to Vibrio cholerae 01, biovar cholerae',
            'category_title':'Malaria', 
        }
        current_url = f'{self.codes_list_url}{self.data.id}/'
        response = self.client.put(current_url,update_data ,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_record_id(self):
        current_url = f'{self.codes_list_url}{self.data.id}/'
        response = self.client.delete(current_url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        
 

    
    


        