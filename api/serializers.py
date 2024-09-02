from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model =Book
        fields =['id','title','author','publish_year','description','bookimg','genres','pdf']
