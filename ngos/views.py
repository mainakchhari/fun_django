# from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def first_view(request: HttpRequest):
    return HttpResponse("OK")
