
from django.urls import path, include

from myapp.views import * 

from . import views 

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name="home"),
    path('employee', views.employee, name="employee"),
    path('employeelist/', views.employeelist, name="employeelist"),
    path('createuser', views.createuser, name="createuser"),
    path('employeedelete/<int:pk>/', views.employeedelete, name="employeedelete"),
    # path('employeedelete/<int:pk>', EmployeedeleteView.as_view(), name="employeedelete"),
    path('loginpage', views.loginpage, name="login"),
    path('applyleave', views.applyleave, name="applyleave"),
    path('payroll/', views.payroll, name="payroll"),

    path('logout', views.logoutUser, name='logoutuser'),
    
]