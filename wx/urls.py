from django.urls import re_path

from rest_framework.documentation import include_docs_urls
from rest_framework.urlpatterns import format_suffix_patterns

from wx.apps import WxConfig

from .views import *


API_TITLE = 'API Documents'
API_DESCRIPTION = 'API Information'

app_name = WxConfig.name


urlpatterns = format_suffix_patterns([
    re_path(r'', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    re_path(r'^wx_login/$', wx_login, name='wx_login'),
    re_path(r'^token/$', JfwTokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^restaurants/$', RestaurantListView.as_view(), name='restaurants'),
    re_path(r'^dish_tags/$', DishTagListView.as_view(), name='dish_tags'),
    re_path(r'^dishes/$', DishListView.as_view(), name='dishes'),
    re_path(r'^companies/$', CompanyListView.as_view(), name='companies'),
    re_path(r'^company_employees/$', CompanyEmployeeListView.as_view(), name='company_employees'),
    re_path(r'^orders/$', OrderListView.as_view(), name='orders'),
    re_path(r'^order_items/$', OrderItemListView.as_view(), name='order_items'),
])
