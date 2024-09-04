from rest_framework_simplejwt.views import TokenObtainPairView
from api import serializers as api_serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db import IntegrityError
from datetime import datetime
import json
import jwt
from django.conf import settings
from users.models import *


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=api_serializers.MyTokenObtainSerializer

   
def authenticate(request):  #Authenticating the token only if they are students
    
    
    if request.method=='GET' or request.method=='POST' or request.method=='PUT' or request.method=='DELETE':

        token=request.headers.get('Authorization',None)
        
        if token==None:
            return {'message':"jwt token is missing...","status":status.HTTP_401_UNAUTHORIZED}
        
        
        scheme,token=token.split(" ")
        
        
        if scheme!='Bearer':
            return {'message':"Wrong Scheme....","status":status.HTTP_400_BAD_REQUEST}
        try:
            
            decoded_token=jwt.decode(token,settings.SECRET_KEY,["HS256"])
        except jwt.InvalidTokenError:
            return {'message':"Invalid Token","status":status.HTTP_401_UNAUTHORIZED}
        
        return decoded_token  
    
    @api_view(['POST'])
    def post_student_details(request):

        decoded_token=authenticate(request)
   
    
        if decoded_token.get('message'):
            message=decoded_token.get('message')
            message_status=decoded_token.get('status')
            return Response({'message':message},status=message_status)
    
    
        student_id = decoded_token.get('user_id')

        first_name = request.data.get('first_name')
        last_name=request.data.get('last_name')
        email=request.data.get('email')
        phone=request.data.get('phone')
        Dateofbirth=request.data.get('Dateofbirth')
        country=request.data.get('country')
        State=request.data.get('State')
        Address=request.data.get('Address')

        try:
            student = Student.objects.get(student_id=student_id)
        except Student.DoesNotExist:
            return Response({'message':f"student with this id -{student_id}"},status=status.HTTP_404_NOT_FOUND)
        
        student.first_name=first_name
        student.last_name=last_name
        student.email=email
        student.phone=phone
        student.Dateofbirth=Dateofbirth
        student.Country=country
        student.State=State
        student.Address=Address
        student.save()


        return Response({'message':'student profile been updated'},status=status.HTTP_200_OK)







        

        