from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class TypeInfo(models.Model):
    name = models.CharField(max_length=5)
    class_name = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=10, default="500g")
    images = models.CharField(max_length=100)
    overview = HTMLField()
    descriptioin = models.CharField(max_length=500)
    stock = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    hot = models.IntegerField()
    type = models.ForeignKey(TypeInfo, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name
