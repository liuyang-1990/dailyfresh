from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1


# Create your views here.
def register(request):
    return render(request, 'df_user/register.html')


def process_register(request):
    user_name = request.POST["user_name"]
    pwd = request.POST["pwd"]
    email = request.POST["email"]
    user = UserInfo()
    user.username = user_name

    psw = sha1()
    psw.update(pwd.encode('utf-8'))
    pwd = psw.hexdigest()
    user.password = pwd
    user.email = email
    user.save()
    return redirect("/user/login")
