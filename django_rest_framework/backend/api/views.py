from django.shortcuts import render
from django.http import JsonResponse
import json


# Create your views here.
def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    return JsonResponse(data)
