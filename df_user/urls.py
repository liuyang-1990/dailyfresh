from django.urls import path
from .views import *

urlpatterns = [
    path('register', register),
    path('process_register', process_register),
    path('register_exist', register_exist),
    path('login', login),
    path('logout', logout),
    path('process_login', process_login),
    path('user_center_info', user_center_info),
    path('user_center_order',user_center_order),
    path('user_center_site', user_center_site),
    path('site_handler', site_handler)
]
