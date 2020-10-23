from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .mail import *
from .db import *
from .models import *


def index(request):
    return render(request, 'main/index.html')


def mail(request):
    if request.method == "POST":
        if verifymail(request.POST['mail']):
            id = uuid.uuid4()
            print(request.build_absolute_uri())
            print(request.get_full_path())
            return redirect('mail:id', id)
        else:
            return render(request, 'main/index.html', context={"error": "Provide a valid mail"})
    else:
        return render(request, 'main/error.html', context={"error": "Invalid Method"})


def id(request, id):
    file = open('id.txt', mode='r')
    if str(id)+'\n' in file.readlines():
        file.close()
        return render(request, 'main/id.html', context={"id": "Session expired"})
    else:
        file = open("id.txt", mode="a", newline='', encoding='UTF-8')
        file.write(str(id)+'\n')
        file.close()
        return render(request, 'main/id.html', context={"id": id})
