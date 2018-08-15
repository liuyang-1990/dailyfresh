from django.urls import path
from .views import *

urlpatterns = [
    path('register', register),
    path('process_register', process_register),
    path('register_exist', register_exist),
    path('login', login),
    path('process_login', process_login)
]
