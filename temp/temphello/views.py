from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def helloworldjson(request):
    json = {"Message": "HELLO WORLD!"}
    return JsonResponse(json)