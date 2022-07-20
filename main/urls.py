from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home/', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('menu/', views.menu,name="menu"),
    path('specials/',views.specials,name="specials"),
    path('events/',views.events,name="events"),
    path('contact/',views.contact,name="contact"),
]