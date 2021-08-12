from django.urls import path
from os_command import views

urlpatterns = [
    path('',views.search),
]