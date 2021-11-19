from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, RocKr!!")

def monthly_challenge(request, month):
    challenges_dict = {"january" : "Eat Healthy", "february" : "Fit Yourself", "march": "Get Fit"}
    if month.lower() in challenges_dict:
        return HttpResponse(challenges_dict.get(month.lower()))
    return HttpResponseNotFound("This Month is not Supported!!")

def monthly_challenge_num(request, month):
    challenges_dict = {1 : "Eat Healthy", 2 : "Fit Yourself", 3: "Get Fit"}
    if month in challenges_dict:
        return HttpResponse(challenges_dict.get(month))
    return HttpResponseNotFound("This Month is not Supported!!")