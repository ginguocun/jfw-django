from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from wx.models import *


class AutoUpdateUserModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by', 'confirmed_by')
    date_hierarchy = 'datetime_created'

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.confirmed_by = user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(DistrictLevel)
class DistrictLevelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'level']
    search_fields = ['level']


@admin.register(ChinaDistrict)
class ChinaDistrictAdmin(admin.ModelAdmin):
    list_display = ['pk', 'city_code', 'ad_code', 'name']
    search_fields = ['city_code', 'ad_code', 'name']


@admin.register(UserLevel)
class UserLevelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'level_code', 'level_name', 'level_desc']
    search_fields = ['level_code', 'level_name', 'level_desc']


@admin.register(Restaurant)
class RestaurantAdmin(AutoUpdateUserModelAdmin):
    list_display = [
        'pk', 'restaurant_name', 'restaurant_code', 'contact_person', 'contact_mobile', 'restaurant_address',
        'is_active', 'created_by', 'confirmed_by']
    search_fields = ['restaurant_name', 'restaurant_code', 'contact_person', 'contact_mobile']


@admin.register(DishTag)
class DishTagAdmin(AutoUpdateUserModelAdmin):
    list_display = ['pk', 'tag_name', 'is_confirmed', 'is_active', 'created_by', 'confirmed_by']
    search_fields = ['tag_name']


@admin.register(Dish)
class DishAdmin(AutoUpdateUserModelAdmin):
    list_display = ['pk', 'title', 'dish_desc', 'price', 'sales']
    search_fields = ['title', 'dish_desc']
    autocomplete_fields = ('restaurant',)
    list_filter = ('dish_tag', 'restaurant')


@admin.register(Company)
class CompanyAdmin(AutoUpdateUserModelAdmin):
    list_display = ['pk', 'company_name', 'company_code', 'company_address']
    search_fields = ['company_name', 'company_code', 'company_address']
    filter_horizontal = ('restaurant',)


@admin.register(CompanyEmployee)
class CompanyEmployeeAdmin(AutoUpdateUserModelAdmin):
    readonly_fields = ('mobile',)
    list_display = ['pk', 'company', 'employee_name', 'mobile', 'user']
    search_fields = ['employee_name', 'mobile']


@admin.register(WxUser)
class WxUserAdmin(UserAdmin):
    readonly_fields = ('last_login', 'date_joined', 'mobile')
    search_fields = [
        'username', 'openid', 'email', 'mobile', 'first_name', 'last_name', 'nick_name', 'company__company_name']
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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'order_code', 'order_date', 'total_price']
    search_fields = ['order_code']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'order', 'dish', 'item_count', 'payed_total_price', 'is_active']