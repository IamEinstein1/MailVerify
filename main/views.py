from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .id import create_id

global id
id = create_id()
file = open('random.txt', mode="r")
content = file.readlines()
# for item in content:
#     if id+'\n' == item:
#         print()


def id_url(request, id):
    file = open('random.txt', mode="r")
    content = file.readlines()
    if str(id+'\n') not in content:
        return HttpResponse("""
    
    
      <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
      integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z"
      crossorigin="anonymous"
    />
  
    
    <h1>Unique id -  {}</h1>""".format(id))
    else:
        return HttpResponse("CODE EXPIRED")


def index(request):
    global id
    return render(request, 'login.html', context={"id": id})


def mail(request):
    global id
    id = create_id()
    return redirect("mail:id", id)


def done(request):
    global id
    return render(request, 'thanks.html')
