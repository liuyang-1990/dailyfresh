from django.urls import path
from .views import *

urlpatterns = [
    path('', cart),
    path('add/<int:gid>/<int:count>', add),
    path('edit/<int:id>/<int:count>', edit),
    path('delete/<int:id>', delete)
]
