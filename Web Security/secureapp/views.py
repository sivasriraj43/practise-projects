from django.shortcuts import render

# Create your views here.

def Home(request):
    
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def dashboard(request):
    return render(request,'dashboard.html')

