from django.urls import path
from .import views

urlpatterns = [
    path("courses/",views.courses),
    path("about/",views.courses),
    path("",views.home)
    
]
