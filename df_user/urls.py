from django.urls import path
from .views import *

urlpatterns = [
    path('register', register),
    path('process_register', process_register)
]
