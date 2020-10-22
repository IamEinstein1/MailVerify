from django.urls import path
from .views import *
app_name = "mail"
urlpatterns = [
    path('', index, name="index"),
    path('mail/', mail, name="mail"),
    path('id/<str:id>', id, name="id")
]
