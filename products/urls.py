from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('shop/', shop, name='shop'),
    path('shop_cate/<int:category>', shop_category, name='shop_category'),
    path('shop_tag/<int:tag>', shop_tag, name='shop_tag'),
    path('single-product/<int:pk>', single_product, name='single_product'),

]
