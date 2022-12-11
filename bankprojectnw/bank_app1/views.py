from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.core.mail import message
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm,NewCreationForm
from .models import District,Branch

# Create your views here.




def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,"home.html")

def registerUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=cpassword)
                user.save();
                return redirect('login')
        else:
            return HttpResponse("password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")
def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username and password:
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse('username or password is incorrect')
        else:
            return HttpResponse('Fill out all the fields')

    return render(request,'login.html')


def create_view(request):
    form=NewCreationForm()
    if request.method=='POST':
        form=NewCreationForm(request.POST)
        if form.is_valid():
            return redirect('new')
    return render(request,'list.html',{'form':form})



def logout(request):
    return HttpResponse('/login')
def new(request):
    return render(request,'new.html')









