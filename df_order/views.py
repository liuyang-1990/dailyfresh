from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import transaction
from df_user.login_decorator import *
from df_user.models import *
from .models import *
from df_cart.models import *
import datetime
from decimal import *


# Create your views here.
@login_check
def order(request):
    cart_id_str = request.GET.get("cart_id")
    cart_ids = cart_id_str.split(",")
    carts = ShoppingCart.objects.filter(id__in=cart_ids)
    user = UserInfo.objects.get(pk=int(request.session["id"]))
    context = {"title": "提交订单", "user": user, "carts": carts, "cart_id": cart_id_str}
    return render(request, "df_order/place_order.html", context)


# 使用事物

@login_check
def order_handler(request):
    cart_id_str = request.POST.get("cart_id")
    cart_ids = cart_id_str.split(",")
    carts = ShoppingCart.objects.filter(id__in=cart_ids)
    tran_id = transaction.savepoint()
    try:
        # 创建订单对象
        now = datetime.datetime.now()
        order = OrderInfo()
        uid = request.session["id"]
        order.order_id = "%s%d" % (now.strftime("%Y%m%d%H%M%S"), uid)
        order.user_id = uid
        order.order_date = now
        order.total = Decimal(request.POST.get("total"))  # 订单总金额
        order.save()
        # with transaction.commit():
        # 创建订单详情
        for cart in carts:
            # cart = ShoppingCart.objects.get(pk=int(id))
            detail = OrderDetail()
            detail.order = order
            goods = cart.goods
            # 库存量大于购买量
            if goods.stock >= cart.count:
                goods.stock = goods.stock - cart.count
                goods.save()
                detail.goods_id = goods.id
                detail.price = goods.price
                detail.count = cart.count
                detail.save()
                cart.delete()
                transaction.savepoint_commit(tran_id)
            else:
                transaction.savepoint_rollback(tran_id)
                return JsonResponse({"data": "2"})  # 库存不足

    except Exception as ex:
        print(ex)
        transaction.savepoint_rollback(tran_id)
        return JsonResponse({"data": ex})
    return JsonResponse({"data": "1"})  # success
