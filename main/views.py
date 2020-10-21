from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .id import create_id

global id
id = create_id()


def idrl(request, id):
    return HttpResponse(f"<h1>Unique id -  {id}</h1>")


def index(request):
    global id
    return render(request, 'index.html', context={"id": id})


def mail(request):
    global id
    return redirect("mail:id", id=create_id())


def done(request):
    global id
    return render(request, 'thanks.html')
