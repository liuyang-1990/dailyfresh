from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from hashlib import sha1


# Create your views here.

def register(request):
    context = {"title": "注册"}
    return render(request, 'df_user/register.html', context)


# 判断用户名是否存在
def register_exist(request):
    uname = request.GET.get("uname")
    count = UserInfo.objects.filter(username=uname).count()
    return JsonResponse({"count": count})


def process_register(request):
    user_name = request.POST["user_name"]
    pwd = request.POST["pwd"]
    email = request.POST["email"]
    user = UserInfo()
    user.username = user_name
    # 加密
    psw = sha1()
    psw.update(pwd.encode('utf-8'))
    pwd = psw.hexdigest()
    user.password = pwd
    user.email = email
    user.save()
    return redirect("/user/login")


def login(request):
    user_name = request.COOKIES.get("user_name", "")
    context = {"title": "登录", "user_name": user_name}
    return render(request, 'df_user/login.html', context)


def process_login(request):
    post = request.POST
    user_name = post.get("username")
    pwd = post.get("pwd")

    user_info = UserInfo.objects.filter(username=user_name)
    if len(user_info) == 1:
        psw = sha1()
        psw.update(pwd.encode('utf-8'))
        pwd = psw.hexdigest()
        if user_info[0].password == pwd:
            response = JsonResponse({"user_error": 0, "pwd_error": 0})
            remeber_me = post.get("remeber", "0")
            if remeber_me == "1":
                response.set_cookie("id", user_info[0].id)
                response.set_cookie("user_name", user_name)
            else:
                response.delete_cookie("id")
                response.delete_cookie("user_name")
            return response
        else:
            return JsonResponse({"user_error": 0, "pwd_error": 1})
    else:
        return JsonResponse({"user_error": 1, "pwd_error": 0})


def user_center_info(request):
    id = request.COOKIES.get("id")
    user = UserInfo.objects.get(pk=id)
    context = {"title": "用户中心", "user": user}
    return render(request, "df_user/user_center_info.html", context)


def user_center_site(request):
    id = request.COOKIES.get("id")
    user = UserInfo.objects.get(pk=id)
    context = {"title": "用户中心", "user": user}
    return render(request, "df_user/user_center_site.html", context)


def site_handler(request):
    post = request.POST
    id = request.COOKIES.get("id")
    user = UserInfo.objects.get(pk=id)
    user.recipients = post.get("recipients", "")
    user.address = post.get("address", "")
    user.postcode = post.get("postcode", "")
    user.mobilephone = post.get("mobilephone", "")
    user.save()
    context = {"title": "用户中心", "user": user}
    return render(request, "df_user/user_center_site.html", context)
