from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
def home_view(request):
    return HttpResponse("Hello, Django Bootcamp!")

def api_view(request):
    data = {
        "message": "Welcome to Django Bootcamp API!",
        "status": "success"
    }
    return JsonResponse(data)
