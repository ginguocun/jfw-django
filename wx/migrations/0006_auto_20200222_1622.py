# Generated by Django 2.2 on 2020-02-22 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wx', '0005_auto_20200222_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='dish_image0',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='dish_image1',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='dish_image2',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='dish_image3',
        ),
        migrations.AddField(
            model_name='dish',
            name='dish_image',
            field=models.ImageField(blank=True, help_text='主照片', null=True, upload_to='dish/', verbose_name='主照片'),
        ),
        migrations.AddField(
            model_name='dish',
            name='dish_image_a',
            field=models.ImageField(blank=True, help_text='照片1', null=True, upload_to='dish/', verbose_name='照片1'),
        ),
        migrations.AddField(
            model_name='dish',
            name='dish_image_b',
            field=models.ImageField(blank=True, help_text='照片2', null=True, upload_to='dish/', verbose_name='照片2'),
        ),
        migrations.AddField(
            model_name='dish',
            name='dish_image_c',
            field=models.ImageField(blank=True, help_text='照片3', null=True, upload_to='dish/', verbose_name='照片3'),
        ),
        migrations.AlterField(
            model_name='chinadistrict',
            name='ad_code',
            field=models.CharField(blank=True, help_text='辖区编号', max_length=100, null=True, verbose_name='辖区编号'),
        ),
        migrations.AlterField(
            model_name='chinadistrict',
            name='center',
            field=models.CharField(blank=True, help_text='中心坐标', max_length=100, null=True, verbose_name='中心坐标'),
        ),
        migrations.AlterField(
            model_name='chinadistrict',
            name='city_code',
            field=models.CharField(blank=True, help_text='电话区号', max_length=100, null=True, verbose_name='电话区号'),
        ),
        migrations.AlterField(
            model_name='chinadistrict',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, help_text='记录时间', verbose_name='记录时间'),
        ),
        migrations.AlterField(
            model_name='chinadistrict',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='chinadistrict',
            name='level',
            field=models.ForeignKey(blank=True, help_text='辖区等级', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx.DistrictLevel', verbose_name='辖区等级'),
        ),
        migrations.AlterField(
            model_name='chinadistrict',
            name='name',
            field=models.CharField(blank=True, help_text='辖区名称', max_length=100, null=True, verbose_name='辖区名称'),
        ),
        migrations.AlterField(
            model_name='chinadistrict',
            name='parent_district',
            field=models.ForeignKey(blank=True, help_text='上级辖区', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx.ChinaDistrict', verbose_name='上级辖区'),
        ),
        migrations.AlterField(
            model_name='company',
            name='center',
            field=models.CharField(blank=True, help_text='中心坐标', max_length=255, null=True, verbose_name='中心坐标'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_address',
            field=models.TextField(blank=True, help_text='企业地址', max_length=2000, null=True, verbose_name='企业地址'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_code',
            field=models.CharField(blank=True, help_text='企业识别码', max_length=255, null=True, unique=True, verbose_name='企业识别码'),
        ),
        migrations.AlterField(
            model_name='company',
            name='confirmed_by',
            field=models.ForeignKey(blank=True, help_text='审核人员', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_confirmed_by', to=settings.AUTH_USER_MODEL, verbose_name='审核人员'),
        ),
        migrations.AlterField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='创建人员', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_created_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人员'),
        ),
        migrations.AlterField(
            model_name='company',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, help_text='记录时间', verbose_name='记录时间'),
        ),
        migrations.AlterField(
            model_name='company',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='company',
            name='is_active',
            field=models.BooleanField(default=False, help_text='有效', verbose_name='有效'),
        ),
        migrations.AlterField(
            model_name='company',
            name='is_confirmed',
            field=models.BooleanField(default=False, help_text='已审核', verbose_name='已审核'),
        ),
        migrations.AlterField(
            model_name='company',
            name='restaurant',
            field=models.ManyToManyField(blank=True, help_text='可见餐馆', related_name='company_related_restaurant', to='wx.Restaurant', verbose_name='可见餐馆'),
        ),
        migrations.AlterField(
            model_name='companyemployee',
            name='confirmed_by',
            field=models.ForeignKey(blank=True, help_text='创建人员', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_employee_confirmed_by', to=settings.AUTH_USER_MODEL, verbose_name='审核人员'),
        ),
        migrations.AlterField(
            model_name='companyemployee',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='创建人员', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_employee_created_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人员'),
        ),
        migrations.AlterField(
            model_name='companyemployee',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, help_text='记录时间', verbose_name='记录时间'),
        ),
        migrations.AlterField(
            model_name='companyemployee',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='companyemployee',
            name='employee_name',
            field=models.CharField(blank=True, help_text='姓名', max_length=200, null=True, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='companyemployee',
            name='is_active',
            field=models.BooleanField(default=False, help_text='有效', verbose_name='有效'),
        ),
        migrations.AlterField(
            model_name='companyemployee',
            name='is_confirmed',
            field=models.BooleanField(default=False, help_text='已审核', verbose_name='已审核'),
        ),
        migrations.AlterField(
            model_name='companyemployee',
            name='mobile',
            field=models.CharField(blank=True, help_text='手机号', max_length=20, null=True, unique=True, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='companyemployee',
            name='user',
            field=models.ForeignKey(blank=True, help_text='用户', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_employee_user', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, help_text='记录时间', verbose_name='记录时间'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_desc',
            field=models.TextField(blank=True, help_text='菜品描述', max_length=2000, null=True, verbose_name='菜品描述'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_name',
            field=models.CharField(blank=True, help_text='商品名称', max_length=255, null=True, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_price',
            field=models.DecimalField(decimal_places=2, default=18.0, help_text='商品价格', max_digits=9, null=True, verbose_name='商品价格'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='is_active',
            field=models.BooleanField(default=True, help_text='是否有效', verbose_name='是否有效'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(blank=True, help_text='餐馆', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx.Restaurant', verbose_name='餐馆'),
        ),
        migrations.AlterField(
            model_name='districtlevel',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, help_text='记录时间', verbose_name='记录时间'),
        ),
        migrations.AlterField(
            model_name='districtlevel',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='districtlevel',
            name='level',
            field=models.CharField(blank=True, help_text='辖区等级', max_length=100, null=True, unique=True, verbose_name='辖区等级'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(blank=True, help_text='用户', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='order',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, help_text='记录时间', verbose_name='记录时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=True, help_text='是否有效', verbose_name='是否有效'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_payed',
            field=models.BooleanField(default=False, help_text='已经支付', verbose_name='已经支付'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_submitted',
            field=models.BooleanField(default=False, help_text='已经提交', verbose_name='已经提交'),
        ),
        migrations.AlterField(
            model_name='order',
            name='item_count',
            field=models.IntegerField(blank=True, help_text='产品数量', null=True, verbose_name='产品数量'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_code',
            field=models.CharField(blank=True, help_text='订单编号', max_length=255, null=True, unique=True, verbose_name='订单编号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, help_text='订单日期', null=True, verbose_name='订单日期'),
        ),
        migrations.AlterField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(blank=True, help_text='餐馆', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx.Restaurant', verbose_name='餐馆'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_discount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='订单折扣', max_digits=9, null=True, verbose_name='订单折扣'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_marked_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='订单标价', max_digits=9, null=True, verbose_name='订单标价'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='订单金额', max_digits=9, null=True, verbose_name='订单金额'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, help_text='记录时间', verbose_name='记录时间'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='dish',
            field=models.ForeignKey(blank=True, help_text='商品', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx.Dish', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='is_active',
            field=models.BooleanField(default=True, help_text='是否有效', verbose_name='是否有效'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item_count',
            field=models.IntegerField(blank=True, help_text='数量', null=True, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='marked_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='标价', max_digits=9, null=True, verbose_name='标价'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, help_text='订单', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx.Order', verbose_name='订单'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='payed_total_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='小计', max_digits=9, null=True, verbose_name='小计'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='payed_unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='单价', max_digits=9, null=True, verbose_name='单价'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='center',
            field=models.CharField(blank=True, help_text='中心坐标', max_length=255, null=True, verbose_name='中心坐标'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='confirmed_by',
            field=models.ForeignKey(blank=True, help_text='审核人员', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_confirmed_by', to=settings.AUTH_USER_MODEL, verbose_name='审核人员'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='contact_mobile',
            field=models.CharField(blank=True, help_text='联系方式', max_length=255, null=True, verbose_name='联系方式'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='contact_person',
            field=models.CharField(blank=True, help_text='联系人', max_length=255, null=True, verbose_name='联系人'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='创建人员', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_created_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人员'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, help_text='记录时间', verbose_name='记录时间'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='is_active',
            field=models.BooleanField(default=False, help_text='有效', verbose_name='有效'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='is_confirmed',
            field=models.BooleanField(default=False, help_text='已审核', verbose_name='已审核'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_address',
            field=models.TextField(blank=True, help_text='餐馆地址', max_length=2000, null=True, verbose_name='餐馆地址'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_code',
            field=models.CharField(blank=True, help_text='餐馆识别码', max_length=255, null=True, verbose_name='餐馆识别码'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_name',
            field=models.CharField(blank=True, help_text='餐馆名称', max_length=255, null=True, unique=True, verbose_name='餐馆名称'),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, help_text='记录时间', verbose_name='记录时间'),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='level_code',
            field=models.SmallIntegerField(blank=True, help_text='等级编号', null=True, unique=True, verbose_name='等级编号'),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='level_desc',
            field=models.TextField(blank=True, help_text='等级描述', max_length=1000, null=True, verbose_name='等级描述'),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='level_name',
            field=models.CharField(help_text='等级名称', max_length=100, null=True, unique=True, verbose_name='等级名称'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='avatar_url',
            field=models.URLField(blank=True, help_text='头像', null=True, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='china_district',
            field=models.ForeignKey(blank=True, help_text='所在辖区', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx.ChinaDistrict', verbose_name='所在辖区'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='city',
            field=models.CharField(blank=True, help_text='城市', max_length=200, null=True, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='company',
            field=models.ForeignKey(blank=True, help_text='公司', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wx_user', to='wx.Company', verbose_name='公司'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='country',
            field=models.CharField(blank=True, help_text='国家', max_length=200, null=True, verbose_name='国家'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='current_role',
            field=models.IntegerField(choices=[(0, '游客'), (1, '客户'), (2, '商家')], default=0, help_text='当前用户角色', null=True, verbose_name='当前用户角色'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='出生日期', null=True, verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, help_text='记录时间', verbose_name='记录时间'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='desc',
            field=models.TextField(blank=True, help_text='描述', max_length=2000, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(1, '男'), (2, '女'), (0, '未知')], help_text='性别', null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='is_client',
            field=models.BooleanField(default=True, help_text='是客户', verbose_name='是客户'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='is_manager',
            field=models.BooleanField(default=False, help_text='是管理员', verbose_name='是管理员'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='is_owner',
            field=models.BooleanField(default=False, help_text='是商家', verbose_name='是商家'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='language',
            field=models.CharField(blank=True, help_text='语言', max_length=100, null=True, verbose_name='语言'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='mobile',
            field=models.CharField(blank=True, help_text='手机号', max_length=100, null=True, unique=True, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='nick_name',
            field=models.CharField(blank=True, help_text='昵称', max_length=100, null=True, unique=True, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='openid',
            field=models.CharField(blank=True, help_text='微信OpenID', max_length=100, null=True, unique=True, verbose_name='微信OpenID'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='province',
            field=models.CharField(blank=True, help_text='省份', max_length=200, null=True, verbose_name='省份'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='restaurant',
            field=models.ForeignKey(blank=True, help_text='餐馆', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx.Restaurant', verbose_name='餐馆'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='user_level',
            field=models.ForeignKey(blank=True, help_text='用户等级', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx.UserLevel', verbose_name='用户等级'),
        ),
    ]