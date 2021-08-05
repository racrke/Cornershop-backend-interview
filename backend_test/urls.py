"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .utils.healthz import healthz
from norasystem.views import *

urlpatterns = [
	path("api/menu", MenuView.as_view(), name="create_menu"),
   	path("api/menu/<uuid:uuid>", MenuView.as_view(), name="show_menu"),
   	path("api/employee", create_employee, name="create_employee"),
   	path("api/request",create_request, name="create_request"), 
   	path("api/report/<uuid:uuid>", show_today, name="show_today"),
    path("healthz", healthz, name="healthz")
]
