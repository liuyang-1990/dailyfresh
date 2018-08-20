from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TypeInfo);


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'images', 'type']
    list_filter = ['type']


admin.site.register(Goods, GoodsAdmin)
