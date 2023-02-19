
from django.shortcuts import render
from . models import Departments,Courses
# Create your views here.
def home_page(request):
    
    return render(request,'index.html')