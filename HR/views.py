from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .utils.calc import calc
from HR.models import Student

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from HR.serializers import Adddataserializer


def hrget(request):
    res=calc(45,47)
    return JsonResponse({'foo':res})
    # return HttpResponse("from hr")
def update(request):
    return HttpResponse("from update")
def delete(request,id):
    return HttpResponse(id)
# @csrf_exempt    
# def addData(request):
   
#     if request.method == 'POST':
#      tutorial_data = JSONParser().parse(request)
#      data_ser=Adddataserializer(data=tutorial_data)
#     if data_ser.is_valid():
#         data_ser.save()
        
#         return JsonResponse(data_ser.data,safe=False)
#     return JsonResponse("failed") 

@csrf_exempt    
def addData(request):
   
    if request.method == 'POST':
     tutorial_data = JSONParser().parse(request)
    return JsonResponse(tutorial_data,safe=False)
               