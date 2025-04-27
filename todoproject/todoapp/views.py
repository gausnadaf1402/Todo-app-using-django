from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from  .models import *
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method=='POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd)
        myuser=User.objects.create_user(fnm,emailid,pwd)
        myuser.save()
        return redirect('/login')
    return render(request,'signup.html')

def login_view(request):
    if request.method=='POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/todo')
        else:
            return redirect('/login')
    return render(request,'login.html')

@login_required(login_url='/login')
def todo(request):
    if request.method=='POST':
        title=request.POST.get('title')
        obj=ToDo(title=title,user=request.user)
        obj.save()
        user=request.user
        res=ToDo.objects.filter(user=user).order_by('-date')
        return redirect('/todo',{'res':res})
    res=ToDo.objects.filter(user=request.user).order_by('-date')
    return render(request,'todo.html',{'res':res})


@login_required(login_url='/login')
def edit_todo(request, sr_no):
    obj = get_object_or_404(ToDo, sr_no=sr_no)
    if request.method == 'POST':
        title = request.POST.get('title')
        print("New title:", title)
        obj.title = title
        obj.save()
        return redirect('/todo/')  # ✅ no context passing here
    return render(request, 'edit_todo.html', {'obj': obj})

@login_required(login_url='/login')
def delete_todo(request,sr_no):
    obj=ToDo.objects.get(sr_no=sr_no)
    obj.delete()
    return redirect('/todo')

def signout(request):
    logout(request)
    return redirect('/login')
