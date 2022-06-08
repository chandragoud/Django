from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
    s="<h1>Welcome to Django</h1>"
    return HttpResponse(s)