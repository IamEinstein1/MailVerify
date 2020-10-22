from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .id import *


def index(request):
    return render(request, 'index.html')


def mail(request):
    if request.method == "POST":
        id = uuid.uuid4()
        print(request.build_absolute_uri())
        print(request.get_full_path())
        return redirect('mail:id', id)
    else:
        return HttpResponse('INVALID METHOD')


def id(request, id):
    file = open('id.txt', mode='r')
    if str(id)+'\n' in file.readlines():
        file.close()
        return HttpResponse('EXPIRED')
    else:
        file = open("id.txt", mode="a", newline='', encoding='UTF-8')
        file.write(str(id)+'\n')
        file.close()
        return HttpResponse(f'RECIEVED - {id}')
