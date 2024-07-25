from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
import random
import string
import json
from django.views.decorators.csrf import csrf_exempt
import requests
from projects.models import NationalFoods


@login_required(login_url='/sign_in/')
def ba(request):
    ba = None
    bas = BrandAmbassador.objects.all()
    if request.method == "POST":
        ref_number = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
        email = request.POST.get("email", "")
        full_name = request.POST.get("full_name", "")
        gender = request.POST.get("gender", "")
        id_number = request.POST.get("id_number", "")
        phone_number = request.POST.get("phone_number", "")

        ba = BrandAmbassador(
            email=email, full_name=full_name, gender=gender, id_number=id_number, phone_number=phone_number,
            ba_code=ref_number.upper(), created_by=request.user.username
        )
        ba.save()

    template = "ba/list_ba.html"
    context = {"ba": bas}
    return render(request, template, context)


@csrf_exempt
def ba_web_service(request):
    get_the_ba = None
    ba_codes = []
    if request.method == "POST":
        data = json.loads(request.body)
        ba_code = data["ba_code"]
        get_the_ba = BrandAmbassador.objects.get(ba_code=ba_code)
        return HttpResponse(json.dumps({"ba_code": get_the_ba.ba_code, "full_name": get_the_ba.full_name} ))


@csrf_exempt
def questionnaire(request):
    if request.method == "POST":
        data = json.loads(request.body)
        customer_phone = data["cPhone"]
        customer_name = data["cName"]
        question1_answer = data["q1"]
        question1_no_reason = data["q1n"]
        question1_yes_reason = data["q1y"]
        question2_answer = data["q2"]
        question3_answer = data["q3"]
        question4_answer = data["q4"]
        question5_answer = data["q5"]
        question6_answer = data["q6"]
        captured_by = data["user"]
        shop = data["shop"]

        add_rec = NationalFoods(
            customer_phone=customer_phone, customer_name=customer_name, question1_answer=question1_answer,
            question1_no_reason=question1_no_reason, question1_yes_reason=question1_yes_reason,
            question2_answer=question2_answer, question3_answer=question3_answer, question4_answer=question4_answer,
            question5_answer=question5_answer, question6_answer=question6_answer, captured_by=captured_by,
            shop=shop
        )
        add_rec.save()
        return HttpResponse("200")
