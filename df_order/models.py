from django.db import models


# Create your models here.

class OrderInfo(models.Model):
    order_id = models.CharField(max_length=32, primary_key=True)
    user = models.ForeignKey('df_user.UserInfo', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    # 0 未付款 1已付款未发货 2已发货
    order_status = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)


class OrderDetail(models.Model):
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    goods = models.ForeignKey('df_goods.Goods', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()
