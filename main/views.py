from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .id import *


def index(request):
    return render(request, 'index.html')


def mail(request):
    id = create_id()

    return HttpResponse(f"NEW ID -{id}")
