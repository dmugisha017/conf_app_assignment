
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    # www.conference.rw/admin/
    path('',views.Home,name='Home'),
    path('create/',views.Form,name='Form'),
    path('<int:id>/',views.Specific,name='Specific'),
    path('<int:id>/update/',views.Update,name='Update'),
     path('<int:id>/delete/',views.Delete,name='Delete'),



]