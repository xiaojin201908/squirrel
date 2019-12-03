from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('nihao')
# Create your views here.
