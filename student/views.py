from typing import Counter
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
import csv

app = "student"


# Create your views here.
def index(request):
    return render(request, 'login.html')


def Login(request):
    if request.method == "POST":
        

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                stu_list = Student.objects.all().order_by('stu_id')
                return render(request, 'masterDashboard.html', {'stu_list': stu_list})
            else:

                return HttpResponseRedirect(reverse(app + ':index'),
                                            {'error_message': '**Your account has been disabled'})
        else:

            return render(request, 'login.html', {'error_message': '**Invalid login. Please try again!!'})

    return render(request, 'login.html')


def Logout(request):
    return HttpResponseRedirect(reverse(app + ':index'))


def add_stu(request):
    print("from add student",request.user)
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse(app + ':index'))
    return render(request, 'add_stu.html')

    #else:
        #return HttpResponseRedirect(reverse(app + ':index'))

def add_stu1(request):
    return render(request, 'add_stu1.html')


def masterDashboard(request):
    stu_list = Student.objects.all().order_by('stu_id')
    return render(request, 'masterDashboard.html', {'stu_list': stu_list})


def add_stu_save(request):
    if request.method == 'POST':
        stu_id = request.POST['stu_id']
        stu_fname = request.POST['stu_fname']
        stu_lname = request.POST['stu_lname']
        stu_Day = request.POST['stu_Day']
        stu_Month = request.POST['stu_Month']
        stu_Year = request.POST['stu_Year']
        stu_contact = request.POST['stu_contact']
        stu_email = request.POST['stu_email']
        stu_room = request.POST['stu_room']
        stu_gender = request.POST['stu_gender']
        Address = request.POST['Address']
        City = request.POST['City']
        Pin_Code = request.POST['Pin_Code']
        State = request.POST['State']
        Country = request.POST['Country']
        COURSES = request.POST['COURSES']
        stu_branch = request.POST['stu_branch']


        Student.objects.create(stu_id=stu_id, stu_fname=stu_fname, stu_lname=stu_lname,stu_Day=stu_Day,
                               stu_Month=stu_Month,stu_Year=stu_Year,stu_email=stu_email,
                               stu_contact=stu_contact,stu_gender=stu_gender,stu_room=stu_room,
                               Address=Address,City=City,Pin_Code=Pin_Code,State=State,Country=Country,
                               COURSES=COURSES,stu_branch=stu_branch,
                               )
        return HttpResponseRedirect(reverse(app + ':masterDashboard'))

def add_stu1_save(request):
    if request.method == 'POST':
        stu_id = request.POST['stu_id']
        stu_fname = request.POST['stu_fname']
        stu_lname = request.POST['stu_lname']
        stu_Day = request.POST['stu_Day']
        stu_Month = request.POST['stu_Month']
        stu_Year = request.POST['stu_Year']
        stu_contact = request.POST['stu_contact']
        stu_email = request.POST['stu_email']
        stu_room = request.POST['stu_room']
        stu_gender = request.POST['stu_gender']
        Address = request.POST['Address']
        City = request.POST['City']
        Pin_Code = request.POST['Pin_Code']
        State = request.POST['State']
        Country = request.POST['Country']
        COURSES = request.POST['COURSES']
        stu_branch = request.POST['stu_branch']

        Student.objects.create(stu_id=stu_id, stu_fname=stu_fname, stu_lname=stu_lname, stu_Day=stu_Day,
                               stu_Month=stu_Month, stu_Year=stu_Year, stu_email=stu_email,
                               stu_contact=stu_contact, stu_gender=stu_gender, stu_room=stu_room,
                               Address=Address, City=City, Pin_Code=Pin_Code, State=State, Country=Country,
                               COURSES=COURSES, stu_branch=stu_branch,
                               )
        return HttpResponseRedirect(reverse(app + ':index'))



def edit_stu(request, stu_id):
    stu = Student.objects.get(stu_id=stu_id)
    return render(request, 'edit_stu.html', {'stu': stu})


def stu_edit_save(request, stu_id):
    stu = Student.objects.get(stu_id=stu_id)
    if request.method == 'POST':
        stu_id = request.POST['stu_id']
        stu_fname = request.POST['stu_fname']
        stu_lname = request.POST['stu_lname']
        stu_Day = request.POST['stu_Day']
        stu_Month = request.POST['stu_Month']
        stu_Year = request.POST['stu_Year']
        stu_contact = request.POST['stu_contact']
        stu_email = request.POST['stu_email']
        stu_room = request.POST['stu_room']
        stu_gender = request.POST['stu_gender']
        Address = request.POST['Address']
        City = request.POST['City']
        Pin_Code = request.POST['Pin_Code']
        State = request.POST['State']
        Country = request.POST['Country']
        COURSES = request.POST['COURSES']
        stu_branch = request.POST['stu_branch']
        stu.stu_id = stu_id
        stu.stu_fname = stu_fname
        stu.stu_lname = stu_lname
        stu.stu_Day = stu_Day
        stu.stu_Month = stu_Month
        stu.stu_Year = stu_Year
        stu.stu_contact = stu_contact
        stu.stu_email = stu_email
        stu.stu_room = stu_room
        stu.stu_gender = stu_gender
        stu.Address = Address
        stu.City = City
        stu.Pin_Code = Pin_Code
        stu.State = State
        stu.Country = Country
        stu.COURSES = COURSES
        stu.stu_branch = stu_branch
        stu.save()
        messages.success(request, "Your Form Is Updated")
        return HttpResponseRedirect(reverse(app + ':masterDashboard'))


def del_stu(request, stu_id):
    stu = Student.objects.get(stu_id=stu_id)
    stu.delete()
    return HttpResponseRedirect(reverse(app + ':masterDashboard'))


def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Reports.csv"'

    writer = csv.writer(response)
    writer.writerow(['ENROLLMENT NO', 'FIRST NAME', 'LAST NAME', 'DOB', 'MOBILE NO','EMAIL ID','ROOM NO',
                     'GENDER','COURSES','BRANCH','ADDRESS','CITY','STATE','PIN CODE','COUNTRY',])
    details = Student.objects.all().order_by('stu_id')

    for detail in details:
        stu_id = detail.stu_id
        stu_fname = detail.stu_fname
        stu_lname = detail.stu_lname
        stu_DOB = detail.stu_Day+detail.stu_Month+detail.stu_Year
        stu_contact = detail.stu_contact
        stu_email = detail.stu_email
        stu_room = detail.stu_room
        stu_gender =detail.stu_gender
        COURSES = detail.COURSES
        stu_branch = detail.stu_branch
        Address = detail.Address
        City = detail.City
        State = detail.State
        Pin_Code = detail.Pin_Code
        Country = detail.Country
        



        done = (stu_id, stu_fname, stu_lname, stu_DOB, stu_contact , stu_email ,stu_room ,
                stu_gender, COURSES, stu_branch, Address, City,  State, Pin_Code, Country, )
        writer.writerow(done)

    return response

def About(request):
    print(request.method)
    if request.method == 'POST':
        About_name = request.POST['name']
        About_mail=request.POST['mail']
        About_text=request.POST['textarea']
        About_me.objects.create(About_me_name=About_name,About_me_mail=About_mail,About_me_text=About_text)
    return render(request,"Aboutme.html")

def show_contact(request):
    data=About_me.objects.all()
    d={"Alldata":data}
    print(data)
    return render(request,"contact.html",d)
    