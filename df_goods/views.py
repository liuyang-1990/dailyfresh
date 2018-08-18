from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    type_infos = TypeInfo.objects.filter(isDelete=False)
    goods_infos = []
    for type in type_infos:
        goods_infos.append(
            Goods.objects.filter(isDelete=False)
                .filter(type_id=type.id)
                .order_by("hot")[:4])
    context = {"title": "首页", "guest_cart": 1, "typeinfos": type_infos, "goosinfo": goods_infos}
    return render(request, "df_goods/index.html", context)
