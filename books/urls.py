from django.urls import path , include
from books import views
urlpatterns = [
    path("",views.home),
    path("main.html",views.main)
]

