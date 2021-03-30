from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from myapp.models import * 

# Create your views here.

def index(request):
    username = request.user.username
    print(username)
    return render(request, 'index.html', {'username': username})



def employee(request):
    employee_details = EmployeeDetails.objects.all()
    total_employee = EmployeeDetails.objects.all().count()

    print(total_employee)
    
    emp_data = {
        'total_employee' : total_employee,
        'employee_details': employee_details,

    }


    # return render(request, 'employee.html', {'employee_details' : employee_details })
    return render(request, 'employee.html', emp_data)


def employeelist(request):
    employee_details = EmployeeDetails.objects.all()

    return render(request, 'employeelist.html', {'employee_details': employee_details})


def createuser(request):

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        print(address)
        email = request.POST.get('email')
        designation = request.POST.get('designation')
        salary = request.POST.get('salary')

        createuser= EmployeeDetails(employee_name=name, address=address, email=email, designation=designation, salary= salary)
        print(createuser)
        createuser.save()

    return render(request, 'createuser.html')

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password = password)

        if user is not None:
            login(request, user)
            return redirect('myapp:home')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def employeedelete(request, pk):

    eid = EmployeeDetails.objects.get(id=pk)
    print(eid, "EID")

    context = {
        'items' : eid,
    }

    if request.method == "POST":
        eid.delete()


    return render(request, 'employeelist.html', context)

def applyleave(request):
    return render(request, 'application.html')

def payroll(request):
    
    return render(request, 'payroll.html')


def logoutUser(request):
    logout(request)
    return redirect('myapp:login')

