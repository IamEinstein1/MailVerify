from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    # path('/mail', mail, name="mail"),
    # path('/sent', sent, name="sent")

]
