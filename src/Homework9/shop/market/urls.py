from django.urls import path
from .api.storeCategory import StoreCategoryView
from .api.purchase import PurchaseView
from .api.item import ItemView
from .api.myBag import MyBagView
from .api.storeOwner import StoreOwnerView
from .api.store import StoreView
from .api.customer import CustomerView
from .api.itemCategory import ItemCategoryView

urlpatterns = [
    path('storeCategory/', StoreCategoryView.as_view()),
    path("storeCategory/<int:id>", StoreCategoryView.check_view),
    path('purchase/', PurchaseView.as_view()),
    path("purchase/<int:id>", PurchaseView.check_view),
    path('item/', ItemView.as_view()),
    path("item/<int:id>", ItemView.check_view),
    path('myBag/', MyBagView.as_view()),
    path("myBag/<int:id>", MyBagView.check_view),
    path('storeOwner/', StoreOwnerView.as_view()),
    path("storeOwner/<int:id>", StoreOwnerView.check_view),
    path('store/', StoreView.as_view()),
    path("store/<int:id>", StoreView.check_view),
    path('customer/', CustomerView.as_view()),
    path("customer/<int:id>", CustomerView.check_view),
    path('itemCategory/', ItemCategoryView.as_view()),
    path("itemCategory/<int:id>", ItemCategoryView.check_view),
]