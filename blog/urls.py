from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path("", views.home, name="home"), 
    path("create/", views.create, name="form_create"), 
]