from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework_simplejwt.tokens import Token

# from .models import *
from users.models import *
from rest_framework import serializers
from django.conf import settings




class StudentSerializer(ModelSerializer):
    class Meta:
        models=Student
        fields=['first_name','last_name','email','phone','Dateofbirth','country','State','Address']
