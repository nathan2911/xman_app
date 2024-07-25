from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


@login_required(login_url='/sign_in/')
def projects(request):
    template = "projects/projects.html"
    context = {}
    return render(request, template, context)


@login_required(login_url='/sign_in/')
def dashboard(request):
    cus = NationalFoods.objects.all()
    template = "dashboard/dashboard.html"
    context = {"cus": cus}
    return render(request, template, context)