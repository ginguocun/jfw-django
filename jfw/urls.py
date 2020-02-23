from django.contrib import admin
from django.urls import re_path, include

from rest_framework.documentation import include_docs_urls

from wx.views import api_root

API_TITLE = 'API Documents'
API_DESCRIPTION = 'API Information'


urlpatterns = [
    re_path(r'^$', api_root),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include('wx.urls', namespace='api')),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]
