from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .id import create_id
# Create your views here.


def id(request, id):

    return HttpResponse(f"<h1>Unique id -  {id}</h1>")


def index(request):
    id = create_id()
    return render(request, 'index.html', context={"id": id})


def mail(request):
    print(request.POST.get('id'))
    print(request.POST)
    return redirect("mail:id", id=create_id())


def done(request):
    return render(request, 'thanks.html')
