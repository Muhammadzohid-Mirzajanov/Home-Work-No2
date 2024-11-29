from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from homework2.templates import *
def views1(request : WSGIRequest):
    return render(request, "index1")
def views2(request : WSGIRequest):
    return render(request, "index2")
def views3(request : WSGIRequest):
    return render(request, "index3")

def views4(request : WSGIRequest):
    return render(request, "index4")

def views5(request : WSGIRequest):
    return render(request, "index5")
def views6(request : WSGIRequest):
    return render(request, "index6")

def views7(request : WSGIRequest):
    return render(request, "index7")

def views8(request : WSGIRequest):
    return render(request, "index8")

def views9(request : WSGIRequest):
    return render(request, "index9")

def views10(request : WSGIRequest):
    return render(request, "index10")
