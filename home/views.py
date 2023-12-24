from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home (request):
    return render(request, 'hotel.html')




def login_page(request):
    if request.method=="POST":
        data=request.POST
        username= data.get('username')
        password= data.get('password')
        user=User.objects.all()
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'User does not exist')
            return redirect('/login/')
            
        user = authenticate(username=username,password=password)
        if user is None:
            messages.warning(request, 'Inavlid credentals')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/home/')
        
        
        
        
            
    return render (request, 'home/templates/login.html')



def register(request):
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        
        user = User.objects.filter(username=username)
        if  user.exists():
            messages.warning(request, 'username already exist')
            return redirect ('/register/')
        else:
            user= User.objects.create(
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request, 'Account created successfully!')
        redirect('/register/')
    return render(request, 'register.html')