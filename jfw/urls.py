from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework.documentation import include_docs_urls


API_TITLE = 'API Documents'
API_DESCRIPTION = 'API Information'


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/', include('wx.urls', namespace='api')),
    re_path(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]
