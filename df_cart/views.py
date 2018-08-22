from django.shortcuts import render, redirect
from django.http import JsonResponse
from df_user.login_decorator import *
from .models import *


# Create your views here.
@login_check
def cart(request):
    user_id = request.session.get("id")
    cart_info = ShoppingCart.objects.filter(user_id=user_id)
    context = {"title": "购物车", "sub_page_name": 1, "cart_info": cart_info}
    return render(request, "df_cart/cart.html", context)


@login_check
def add(request, gid, count):
    user_id = request.session.get("id")
    carts = ShoppingCart.objects.filter(user_id=user_id, goods_id=gid)
    if len(carts) > 0:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = ShoppingCart()
        cart.user_id = user_id
        cart.goods_id = gid
        cart.count = count
    cart.save()
    if request.is_ajax():
        total = ShoppingCart.objects.filter(user_id=user_id).count()
        return JsonResponse({"count": total})
    return redirect('/cart/')


@login_check
def edit(request, id, count):
    try:
        cart = ShoppingCart.objects.get(pk=id)
        cart.count = count
        cart.save()
    except Exception as e:
        return JsonResponse({"msg": e})
    return JsonResponse({"msg": "ok"})


@login_check
def delete(request, id):
    try:
        cart = ShoppingCart.objects.get(pk=id)
        cart.delete()
    except Exception as e:
        return JsonResponse({"msg": e})
    return JsonResponse({"msg": "ok"})
