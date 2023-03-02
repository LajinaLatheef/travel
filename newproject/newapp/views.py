from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import Travel
from.models import Team


# Create your views here.
def demo(request):
    obj=Travel.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'results':obj1})

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect ("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect ("register")
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)


                user.save()
                return redirect('login')
            # print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect("register")

        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res1=x+y
#     res2=x-y
#     return render(request,"about.html",{'result1':res1,'result2':res2})

# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("hello am contact")