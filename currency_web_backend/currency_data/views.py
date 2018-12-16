from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# api

def here(request):
    return HttpResponse('Hello World!')