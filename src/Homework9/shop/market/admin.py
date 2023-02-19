from django.contrib import admin
from .models import *
# Register your models here.


class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "picture")
    search_fields = ['id']


class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "picture")
    search_fields = ['id']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "avatar", "registered_at")
    search_fields = ['id']


class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ("id", "avatar", "registered_at")
    search_fields = ['id']


class StoreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ['id']


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "picture", "price", "quantity", "info")
    search_fields = ['id']


class MyBagAdmin(admin.ModelAdmin):
    list_display = ("id", "total_price")
    search_fields = ['id']


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("id", "buy_time", "total_price")
    search_fields = ['id']


admin.site.register(StoreCategory, StoreCategoryAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(StoreOwner, StoreOwnerAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(MyBag, MyBagAdmin)
admin.site.register(Purchase, PurchaseAdmin)