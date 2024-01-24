from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view,permission_classes
from django.http import JsonResponse, HttpResponse
import re
from rest_framework.response import Response

from django.http import HttpResponse
from rest_framework.status import (
  HTTP_400_BAD_REQUEST,
  HTTP_404_NOT_FOUND,
  HTTP_200_OK,
)


@csrf_exempt
@api_view(["POST"])
def getGOAuthToken(request):
  print("Helooooo")
  user_data = request.data
  user_token =  user_data['user_token']
  if user_token is None:
    return Response(None, status=HTTP_400_BAD_REQUEST)
  else:
    return Response(None,status=HTTP_200_OK)
  
