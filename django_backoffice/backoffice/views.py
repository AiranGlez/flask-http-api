import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to our Django project")

def get_data(request):
    response = requests.get('http://localhost:5000/steam')

    print(type(response))
    
    if response.status_code == 200:
        return HttpResponse(response)