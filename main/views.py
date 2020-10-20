from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def mail(request):
    pass


def done(request):
    return render(request, 'thanks.html')
