from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from wx.models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_code', 'company_address']
    search_fields = ['company_name', 'company_code', 'company_address']


@admin.register(ChinaDistrict)
class ChinaDistrictAdmin(admin.ModelAdmin):
    list_display = ['city_code', 'ad_code', 'name']
    search_fields = ['city_code', 'ad_code', 'name']


@admin.register(UserLevel)
class UserLevelAdmin(admin.ModelAdmin):
    list_display = ['level_code', 'level_name', 'level_desc']
    search_fields = ['level_code', 'level_name', 'level_desc']


@admin.register(WxUser)
class WxUserAdmin(UserAdmin):
    readonly_fields = ('last_login', 'date_joined')
    search_fields = [
        'username', 'openid', 'mobile', 'email', 'first_name', 'last_name', 'nick_name', 'company__company_name']
    list_filter = ['is_owner', 'is_client', 'is_manager']
    autocomplete_fields = ['company', 'china_district', 'user_level']
    fieldsets = (
        (_('基础信息'), {'fields': ('username', 'password', 'openid')}),
        (_('个人信息'), {'fields': (
            'nick_name', 'first_name', 'last_name', 'avatar_url', 'gender', 'date_of_birth', 'desc')}),
        (_('联络信息'), {'fields': ('mobile', 'email',)}),
        (_('角色信息'), {'fields': ('is_owner', 'is_client', 'is_manager')}),
        (_('地址信息'), {'fields': ('city', 'province', 'country', 'china_district')}),
        (_('分类信息'), {'fields': ('user_level', 'company')}),
        (_('登录信息'), {'fields': ('last_login', 'date_joined')}),
    )
