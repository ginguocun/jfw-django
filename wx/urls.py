from wx.apps import WxConfig
from .views import *
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

app_name = WxConfig.name

urlpatterns = format_suffix_patterns([
    re_path(r'^wx_login/$', wx_login, name='wx_login'),
    re_path(r'^companies/$', CompanyListView.as_view(), name='companies'),
    re_path(r'^token/$', JfwTokenObtainPairView.as_view(), name='token_obtain_pair'),
])
