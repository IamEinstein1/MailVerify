# from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .mail import *
from .db import *
from .models import *
from django.db.utils import IntegrityError


def index(request):
    check_if_key_is_valid(Id)
    return render(request, 'main/index.html')


def mail(request):
    check_if_key_is_valid(Id)
    if request.method == "POST":
        if verifymail(request.POST['mail']):
            # To get the location
            ip = request.META.get('REMOTE_ADDR', None)

            import uuid
            id = Id.objects.create()
            id.unique_id = uuid.uuid4()
            id.ip = ip
            # id.time_created = datetime.now()
            mail = request.POST['mail']
            for item in Id.objects.all():
                if item.mail == mail:
                    return render(request, 'main/index.html', context={"error": "You have already registered"})
                else:
                    pass

            try:
                id.mail = mail
            except IntegrityError:
                return render(request, 'main/index.html', context={"error": "You have already registered"})
            id.save()
            return redirect('mail:id', id.unique_id)
        else:
            return render(request, 'main/index.html', context={"error": "Provide a valid mail"})
    else:
        return render(request, 'main/error.html', context={"error": "Invalid Method"})


def id(request, id):
    check_if_key_is_valid(Id)
    try:
        return render(request, 'main/id.html', context={"id": id})
    except (Id.DoesNotExist, KeyError):
        return render(request, 'main/id.html', context={"id": "Session Expireds"})
