from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('jobs/',views.myjobs),
    path('news/',views.news),
    path('videos/',views.videos),
    path('viewnews/',views.viewnews),
    path('me/',views.aboutme),



]