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
            ip = request.META.get('REMOTE_ADDR', None)
            import uuid
            id = Id.objects.create()
            id.unique_id = uuid.uuid4()
            id.ip = ip
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
            return redirect('mail:sent', id.unique_id)
        else:
            return render(request, 'main/index.html', context={"error": "Provide a valid mail"})
    else:
        return render(request, 'main/error.html', context={"error": "Invalid Method"})


def id(request, id):
    check_if_key_is_valid(Id)
    for i in Id.objects.all():
        if id in i.unique_id:
            try:
                global valid
                valid = True
            except (Id.DoesNotExist, KeyError):
                valid = False
        elif id not in i.unique_id:
            valid = False
    if valid == False:
        return render(request, 'main/id.html', context={"id": "Session Expired/ID not valid"})
    else:
        return render(request, 'main/id.html', context={"id": id})
        # return render(request, 'main/sent.html')


def sent(request, *args):
    check_if_key_is_valid(Id)
    return render(request, 'main/sent.html', context={"id": id})
