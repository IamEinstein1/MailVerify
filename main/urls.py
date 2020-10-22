from django.urls import path
urlpatterns = [
    path('', index, name="index"),
    path('/mail', mail, name="mail"),
    path('/sent', sent, name="sent")

]
