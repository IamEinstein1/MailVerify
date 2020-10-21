from django.urls import path
from .views import *
app_name = "mail"
urlpatterns = [

    path('', index, name="index"),
    path('mail/', mail, name="mail"),
    path('done/', done, name="done"),
    path('id/<str:id>', idrl, name='id')
]
# print(urlpatterns)
