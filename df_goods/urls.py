from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('list/<int:type_id>/<int:sort_id>/<int:page_index>', list),
    path('detail/<int:id>', detail)
]
