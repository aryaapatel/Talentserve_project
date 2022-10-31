# Create your views here.
# i have created this file

from django.shortcuts import render,redirect
from .models import Index
from django.core.mail import EmailMessage
from django.conf import settings


def index(request):
    if request.method == "POST":
       employeeid = request.POST.get('employeeid')
      # department = request.POST.get('department')
       fullname = request.POST.get('fullname')
       emailid = request.POST.get('emailid')
       concern = request.POST.get('concern')
       emp = Index(employeeid=employeeid, fullname=fullname, emailid=emailid, concern=concern)
       emp.save()
    return render(request,'index.html')

def user_info(request):
	myuser=request.POST.get('email')
	mypass=request.POST.get('pass')

	if (myuser=='admin' and mypass=='arya21'): # username= admin and password= arya21
		return redirect('/response/')
	else:
		return redirect('/index/')

def homepage1(request):
    return render(request,'admin_response.html')

def homepage(request):
    return render(request,'login.html')

def EmployeeData(request):
	# stud = Student.objects.all()
	data =Index.objects.all()
	# print("Myoutput",data)
	context={'data':data}
	return render(request,'EmployeeData.html',context)

def logout(request):
	return render(request,'logout.html')


def email_info(request):
    myto = request.POST.get('to')
    mysubject = request.POST.get('subject')
    mymessage = request.POST.get('msg')
    email = EmailMessage(mysubject, mymessage, settings.EMAIL_HOST_USER, [myto])
    email.content_subtype = 'html'
    email.send()
    return redirect('/response/')

    # send_mail(mysubject,mymessage,settings.EMAIL_HOST_USER,[myto], fail_silently=False)
    # messages.success(request,'Email Sent Successfully')


