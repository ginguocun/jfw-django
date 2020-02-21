from wx.apps import WxConfig
from .views import *
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

app_name = WxConfig.name

urlpatterns = format_suffix_patterns([
    re_path(r'^wx_login/$', wx_login, name='wx_login'),
    re_path(r'^token/$', JfwTokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^restaurants/$', RestaurantListView.as_view(), name='restaurants'),
    re_path(r'^dishes/$', DishListView.as_view(), name='dishes'),
    re_path(r'^companies/$', CompanyListView.as_view(), name='companies'),
    re_path(r'^orders/$', OrderListView.as_view(), name='orders'),
    re_path(r'^order_items/$', OrderItemListView.as_view(), name='order_items'),
])
