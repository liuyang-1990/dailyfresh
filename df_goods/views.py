from django.shortcuts import render
from .models import *
from df_cart.models import ShoppingCart
from haystack.generic_views import *


# Create your views here.
def index(request):
    type_infos = TypeInfo.objects.filter(isDelete=False)
    goods_infos = []
    for type in type_infos:
        goods_infos.append(
            Goods.objects.filter(isDelete=False)
                .filter(type_id=type.id)
                .order_by("hot")[:4])
    count = cart_count(request)
    context = {"title": "首页",
               "guest_cart": 1,
               "typeinfos": type_infos,
               "cart_count": count,
               "goosinfo": goods_infos}
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
    count = cart_count(request)
    page = paginator.page(page_index)
    context = {"title": "商品列表", "guest_cart": 1,
               "typeinfos": type_infos, "type_info": type_info,
               "new_goods": new_goods,
               "sort_id": sort_id,
               "page": page,
               "cart_count": count,
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
    count = cart_count(request)
    context = {"title": "商品详情", "guest_cart": 1,
               "typeinfos": type_infos,
               "type_info": type_info,
               "new_goods": new_goods,
               "cart_count": count,
               "goods_info": goods_info}
    response = render(request, 'df_goods/detail.html', context)

    # 最近浏览 5个商品
    id = str(id)
    goods_ids_str = request.COOKIES.get("goods_ids", "")
    goods_ids = []
    if goods_ids_str == "":
        goods_ids.insert(0, id)
    else:
        goods_ids = goods_ids_str.split(",")
        if id in goods_ids:
            goods_ids.remove(id)
            goods_ids.insert(0, id)
        else:
            goods_ids.insert(0, id)
    if len(goods_ids) > 5:
        goods_ids.pop()
    response.set_cookie("goods_ids", ",".join(goods_ids))

    return response


def cart_count(request):
    user_id = request.session.get("id")
    if user_id is None:
        return 0
    count = ShoppingCart.objects.filter(user_id=user_id).count()
    return count


class MySearchView(SearchView):
    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        type_infos = TypeInfo.objects.filter(isDelete=False)
        context["title"] = "全文搜索"
        context["guest_cart"] = 1
        context["typeinfos"] = type_infos
        context["cart_count"] = cart_count(self.request)
        return context
