from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [

     path('', views.homepage, name="homepage"),
     path('user_info/', views.user_info, name='user_info'),
     path('index/', views.index, name="index"),
     path('response/', views.homepage1,name='response'),
     path('EmployeeData/',views.EmployeeData,name='EmployeeData'),
     path('logout/',views.logout,name='logout'),
     path('email_info/', views.email_info, name='email_info'),

              ]
