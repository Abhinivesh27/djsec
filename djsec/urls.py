from django.contrib import admin
from django.urls import path, include
from os_command import urls
import os_command

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('os_command.urls'))
]
