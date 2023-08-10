"""
URL configuration for inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

from demo.apiview import add_inventory, fetch_pending_inventory, approve_inventory

urlpatterns = [
    path('demo/',include('demo.urls')),
    path('api/add-inventory/', add_inventory),
    path('api/fetch-pending-inventory/', fetch_pending_inventory),
    path('api/approve-inventory/<int:inventory_id>/', approve_inventory),
]
