from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,logout

from django.contrib import messages
# Create your views here.


# message =[
#     {"name":"gokul","email":"gokul@gmail.com"}
# ]
def logout(request):

    auth.logout(request)
    return redirect("/")



def index(request):

    return render(request,"index.html")

def logging(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        global user
        user = authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("http://127.0.0.1:8000/ronin/dropdown/")
        else:
            messages.info(request, 'Wrong username or password')
            return redirect("http://127.0.0.1:8000/ronin/login/")
    else:
        return render(request,'login.html')


def sports(request):
    if request.method == 'POST':
        username= request.POST['username']
        passowrd= request.POST['password']
        user = authenticate(username=username,passowrd=passowrd)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credientials")
            return redirect('sports')
    else:
        return render(request,'sports_index.html')

def table(request):
    return render(request,"table.html")
def insert(request):
    if request.method=='POST':
        student_id=request.POST['student_id']
        student_name=request.POST['student_name']
        student_year=request.POST['student_year']
        student_sports=request.POST['student_sports']

        obj=all_students_info()
        obj.id=student_id
        obj.name=student_name
        obj.year=student_year
        obj.sports_tag=student_sports
        obj.save()

    return render(request,'insert.html')
def delete(request):
    if request.method=='POST':
        student_id=request.POST['recordId']
        obj=all_students_info.objects.get(id=student_id)
        obj.delete()
    return render(request,'delete.html')
def update(request):
    if request.method=='POST':
        student_id=request.POST['recordId']
        student_name=request.POST['newName']
        student_year=request.POST['newYear']
        student_sports=request.POST['newSport']
        obj=all_students_info.objects.get(id=student_id)
        obj.name=student_name
        obj.year=student_year
        obj.sports_tag=student_sports
        obj.save()
    return render(request,'update.html')
@login_required
def dropdown(request):
    return render(request,"dropdown.html")

def results(request):
    if request.GET['sports']=='kabadi':
        message=kabadi.objects.all()
    elif request.GET['sports']=='cricket': 
        message=cricket.objects.all()   
    elif request.GET['sports']=='football': 
        message=football.objects.all()
    elif request.GET['sports']=='basketball':
        message=basketball.objects.all()
    elif request.GET['sports']=='khokho':
        message=khokho.objects.all()
    context = {
        'message': message,
    }
    return render(request, 'results.html', context)
