from django.db import models


# Create your models here.
class ShoppingCart(models.Model):
    user = models.ForeignKey('df_user.UserInfo', on_delete=models.DO_NOTHING)
    goods = models.ForeignKey('df_goods.Goods', on_delete=models.DO_NOTHING)
    count = models.IntegerField()
