from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return{
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


def registerview(request):
    if request.method =='POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,f'Account Created for {user.username}!')

            tokens =get_tokens_for_user(user)

            return redirect('home')
        else:
            form=UserRegisterForm()
        return Response({'message':'details registered'},status=status.HTTP_200_OK)

