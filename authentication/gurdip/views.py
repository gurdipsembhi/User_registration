from django.shortcuts import render,redirect    
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1==pass2:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
        
            return redirect('login')
        else:
            return redirect('signup')
        # print(uname,email,pass1,pass2)
    return render(request,'signup.html')
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        # print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            # return HttpResponse('user not found ')
            return redirect('signup')
    return render(request,'login.html')
def logoutpage(request):
    logout(request)
    return redirect('login')