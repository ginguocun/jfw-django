from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from wx.models import *

admin.site.site_header = '金饭碗后台管理系统'
admin.site.site_title = '金饭碗'
admin.site.index_title = '金饭碗后台管理系统'


class GeneralModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'datetime_created'


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
class DistrictLevelAdmin(GeneralModelAdmin):
    list_display = ['pk', 'level']
    search_fields = ['level']


@admin.register(ChinaDistrict)
class ChinaDistrictAdmin(GeneralModelAdmin):
    list_display = ['pk', 'city_code', 'ad_code', 'name']
    search_fields = ['city_code', 'ad_code', 'name']


@admin.register(UserLevel)
class UserLevelAdmin(GeneralModelAdmin):
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
    list_display = ['pk', 'title', 'dish_desc', 'tags', 'price', 'sales', 'rate_count', 'rate_score', 'is_active']
    search_fields = ['title', 'dish_desc']
    autocomplete_fields = ('restaurant',)
    list_filter = ('restaurant', 'dish_tag', 'is_active')
    filter_horizontal = ('dish_tag',)


@admin.register(Company)
class CompanyAdmin(AutoUpdateUserModelAdmin):
    list_display = ['pk', 'company_name', 'company_code', 'company_address']
    search_fields = ['company_name', 'company_code', 'company_address']
    filter_horizontal = ('restaurant',)
    list_filter = ['is_confirmed', 'is_active']


@admin.register(CompanyEmployee)
class CompanyEmployeeAdmin(AutoUpdateUserModelAdmin):
    readonly_fields = ('mobile_data', 'mobile_index', 'created_by', 'confirmed_by')
    list_display = ['pk', 'company', 'employee_name', 'employee_code', 'user']
    search_fields = ['company__company_name', 'employee_name', 'employee_code', 'mobile_index']
    autocomplete_fields = ['company', 'user']
    list_filter = ['is_confirmed', 'is_active']

    fieldsets = (
        (_('基础信息'), {'fields': ('company', 'employee_name', 'employee_code', 'mobile_index', 'user')}),
        (_('状态信息'), {'fields': ('is_confirmed', 'is_active', 'created_by', 'confirmed_by')}),
    )


@admin.register(WxUser)
class WxUserAdmin(UserAdmin):
    readonly_fields = (
        'last_login', 'date_joined', 'mobile_data', 'mobile_index',
        'nick_name', 'city', 'province', 'country', 'china_district', 'avatar_url'
    )
    search_fields = [
        'username', 'openid', 'email', 'mobile_index', 'first_name', 'last_name', 'nick_name', 'company__company_name']
    list_filter = ['is_owner', 'is_client', 'is_manager']
    autocomplete_fields = ['company', 'china_district', 'user_level']
    fieldsets = (
        (_('基础信息'), {'fields': ('username', 'password', 'openid')}),
        (_('个人信息'), {'fields': (
            'nick_name', 'first_name', 'last_name', 'avatar_url', 'gender', 'date_of_birth', 'desc')}),
        (_('联络信息'), {'fields': ('mobile_index', 'email',)}),
        (_('角色信息'), {'fields': ('is_owner', 'is_client', 'is_manager')}),
        (_('地址信息'), {'fields': ('city', 'province', 'country', 'china_district')}),
        (_('分类信息'), {'fields': ('user_level', 'company')}),
        (_('登录信息'), {'fields': ('last_login', 'date_joined')}),
    )


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    exclude = ['rate_notes', 'is_rated']
    autocomplete_fields = ['dish']


@admin.register(Order)
class OrderAdmin(GeneralModelAdmin):
    date_hierarchy = 'order_date'
    list_display_links = ['pk', 'order_code']
    list_display = ['pk', 'order_code', 'order_date', 'deliver_time', 'total_marked_price', 'total_price', 'order_type']
    list_filter = ['order_type', 'order_date']
    search_fields = ['order_code', 'restaurant__restaurant_name', 'client__nick_name']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(GeneralModelAdmin):
    list_display = ['pk', 'order', 'dish', 'item_count', 'payed_total_price', 'is_active']
    search_fields = ['dish__title', 'order__order_code']
    list_filter = ['is_active']
