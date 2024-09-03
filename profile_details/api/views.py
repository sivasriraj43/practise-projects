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

        first_name = request.data.get('first_name')
        last_name=request.data.get('last_name')
        email=request.data.get('email')
        phone=request.data.get('phone')
        Dateofbirth=request.data.get('Dateofbirth')
        country=request.data.get('country')
        state=request.data.get('State')
        Address=request.data.get('Address')


        return Response({'message':'student profile been updated'})







        

        