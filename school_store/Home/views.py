from django.shortcuts import redirect, render
from . models import Departments,Courses
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def home_page(request):
    departments=Departments.objects.all()
    return render(request,'index.html',{'departments':departments})

#function for signup

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already taken')
            else :
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else :
            messages.error(request,'Password not matching')
    return render(request,'signup.html')

# function for login
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else :
            messages.error(request,'Invalid Username or Password')
            return redirect('login')
    return render(request,'login.html')

# function to log out