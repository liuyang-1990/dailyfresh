from django.core.paginator import Paginator
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


def list(request, type_id, sort_id, page_index):
    type_infos = TypeInfo.objects.filter(isDelete=False)
    type_info = TypeInfo.objects.get(pk=type_id)
    new_goods = type_info.goods_set.order_by("-id")[0:2]
    if sort_id == 1:
        good_list = Goods.objects.filter(isDelete=False).filter(type_id=type_id).order_by("-id")
    elif sort_id == 2:
        good_list = Goods.objects.filter(isDelete=False).filter(type_id=type_id).order_by("-price")
    elif sort_id == 3:
        good_list = Goods.objects.filter(isDelete=False).filter(type_id=type_id).order_by("-hot")
    else:
        pass
    paginator = Paginator(good_list, 10)
    page = paginator.page(page_index)
    context = {"title": "商品列表", "guest_cart": 1,
               "typeinfos": type_infos, "type_info": type_info,
               "new_goods": new_goods,
               "sort_id": sort_id,
               "page": page,
               "paginator": paginator
               }
    return render(request, "df_goods/list.html", context)


def detail(request, id):
    type_infos = TypeInfo.objects.filter(isDelete=False)
    goods_info = Goods.objects.get(pk=id)
    goods_info.hot = goods_info.hot + 1
    goods_info.save()
    type_info = goods_info.type
    new_goods = goods_info.type.goods_set.order_by("-id")[0:2]
    context = {"title": "商品详情", "guest_cart": 1,
               "typeinfos": type_infos,
               "type_info": type_info,
               "new_goods": new_goods,
               "goods_info": goods_info}

    return render(request, 'df_goods/detail.html', context)
