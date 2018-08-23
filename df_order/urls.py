from django.urls import path
from .views import *

urlpatterns = [
    path('place_order', order),
    path('order_handler', order_handler)
]
