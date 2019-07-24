# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from testApp.models import Employee
from . import forms

# for Login forms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required






# from forms import UserProfieInfoForm,UserForm
# Create your views here.
def empdata(request):
    # emp_list = Employee.objects.all()
    emp_list = Employee.objects.order_by('eno')
    my_dict = {'emp_list':emp_list}
    return render(request,'testApp/emp.html',context=my_dict)

def form_view(request):
    form = forms.simpleForm()
    if request.method =="POST":
        form = forms.simpleForm(request.POST)
        if form.is_valid():
            print("form is render")
            print("Name is got "+form.cleaned_data['name'])
            # print("Name is got "+form.cleaned_data['email'])

    return render(request,'testApp/basicApp.html', {'form':form})

def empty_page(request):
    return render(request,'testApp/testpage.html')


# for forms
def index(request):
    return render(request,'testApp/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('register'))

@login_required
def special(request):
    return render(request,'testApp/special.html',{})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form  = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user  #onr to onr filed linking in view
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form= forms.UserForm()
        profile_form  = forms.UserProfileInfoForm()

    return render(request,'testApp/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


# for login
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('special'))
            else:
                return HttpResponse("Account Not Active!..")
        else:
            print("some one tried to login and failed!..")
            print("Username {} and Password {}",format(username,password))
            print("Invalid Login details Supplied!..")
    else:
        return render(request,'testApp/user_login.html',{} )
