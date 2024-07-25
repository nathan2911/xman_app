from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate


def sign_in(request):
    msg = ""
    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to='/projects/')
    if request.method == "POST":
        if request.user.is_authenticated:
            return HttpResponseRedirect(redirect_to='/projects/')
        else:
            postdata = request.POST.copy()
            usrname = postdata.get('username')
            pwd = postdata.get('password')
            new_user = authenticate(username=usrname, password=pwd)
            if new_user and new_user.is_active:
                login(request, new_user)
                return HttpResponseRedirect(redirect_to='/projects/')

            else:
                template = "auth/login.html"
                msg = "Username or Password is wrong. Please try again."
                context = {"msg": msg}
                return render(request, template, context)
    return render(request, 'auth/login.html')


def user_logout(request):
    logout(request)
    return redirect('/')