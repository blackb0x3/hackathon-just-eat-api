from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
# Create your views here.
@api_view(["POST"])
def IdealWeight(heightdata):
#The IdealWeight(heightdate) is the method that gets executed when API call is made. It has a simple logic to calculate weight(=height*10). The line return JsonRespone(…) will send the response back.
    try:
        height=json.loads(heightdata.body)
        weight=str(height*10)
        return JsonResponse("Ideal weight should be:"+ weight +" kg",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

# Create your views here.
def login(request):
    return JsonResponse("Reached login endpoint")

def register(request):
    return JsonResponse("Reached register endpoint")

def getAccountDetails(request, account_id=None):
    if account_id is None:
        return JsonResponse({
            "success": False,
            "reason": "No account ID"
        })

    return JsonResponse("Reached account-details endpoint")

def updateAccountDetails(request, account_id=None):
    if account_id is None:
        return JsonResponse({
            "success": False,
            "reason": "No account ID"
        })

    return JsonResponse("Reached update-account endpoint")

def getRequests(request, account_id=None):
    if account_id is None:
        return JsonResponse({
            "success": False,
            "reason": "No account ID"
        })

    return JsonResponse("Reached requests endpoint (for food that is...)")
