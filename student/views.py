from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Student
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
    return render(request, 'add_stu.html')


def masterDashboard(request):
    stu_list = Student.objects.all().order_by('stu_id')
    return render(request, 'masterDashboard.html', {'stu_list': stu_list})


def add_stu_save(request):
    if request.method == 'POST':
        stu_id = request.POST['stu_id']
        stu_fname = request.POST['stu_fname']
        stu_lname = request.POST['stu_lname']
        stu_branch = request.POST['stu_branch']
        stu_age = request.POST['stu_age']
        stu_contact = request.POST['stu_contact']

        Student.objects.create(stu_id=stu_id, stu_fname=stu_fname, stu_lname=stu_lname,
                                stu_branch=stu_branch, stu_age=stu_age, stu_contact=stu_contact)
        return HttpResponseRedirect(reverse(app + ':masterDashboard'))


def edit_stu(request, stu_id):
    stu = Student.objects.get(stu_id=stu_id)
    return render(request, 'edit_stu.html', {'stu': stu})


def stu_edit_save(request, stu_id):
    stu = Student.objects.get(stu_id=stu_id)
    if request.method == 'POST':
        stu_id = request.POST['stu_id']
        stu_fname = request.POST['stu_fname']
        stu_lname = request.POST['stu_lname']
        stu_branch = request.POST['stu_branch']
        stu_age = request.POST['stu_age']
        stu_contact = request.POST['stu_contact']
        stu.stu_id = stu_id
        stu.stu_fname = stu_fname
        stu.stu_lname = stu_lname
        stu.stu_branch = stu_branch
        stu.stu_age = stu_age
        stu.stu_contact = stu_contact
        stu.save()
        return HttpResponseRedirect(reverse(app + ':masterDashboard'))


def del_stu(request, stu_id):
    stu = Student.objects.get(stu_id=stu_id)
    stu.delete()
    return HttpResponseRedirect(reverse(app + ':masterDashboard'))


def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Reports.csv"'

    writer = csv.writer(response)
    writer.writerow(['Student Id', 'First Name', 'Last Name', 'branch', 'Age', 'contact'])
    details = Student.objects.all().order_by('stu_id')

    for detail in details:
        stu_id = detail.stu_id
        stu_fname = detail.stu_fname
        stu_lname = detail.stu_lname
        stu_branch = detail.stu_branch
        stu_age = detail.stu_age
        stu_contact = detail.stu_contact

        done = (stu_id, stu_fname, stu_lname, stu_branch, stu_age, stu_contact)
        writer.writerow(done)

    return response




