from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("home url")

def sobre(request):
    return HttpResponse("sobre url")

def contato(request):
    return HttpResponse("contato url")