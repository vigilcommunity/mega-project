import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from vigil_ctf_app.EmailBackEnd import EmailBackEnd

#Authentication views ONLY ONLY
def register(request):
    return render(request,'authentication/signup.html')

def show_login(request):
    return render(request,'authentication/signin.html')

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('admin')
        else:
            messages.error(request,"Invalid User Details")
            return HttpResponseRedirect("/")



def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")


def policy(request):
    return render(request,'rules/policy.html')

