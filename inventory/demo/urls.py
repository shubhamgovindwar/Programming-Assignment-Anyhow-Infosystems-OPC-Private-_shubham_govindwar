from django.urls import path
from .views import *

urlpatterns = [
    path('add_inventory/',add_inventory),
    path('signup/', signup),
    path('fetch_pending_inventory/',fetch_pending_inventory),
    path('approve-inventory/',approve_inventory),
    path('login/', user_login),


]