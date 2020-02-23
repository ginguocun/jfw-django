from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


role_choices = [(0, '游客'), (1, '客户'), (2, '商家')]
admin.site.site_header = '金饭碗后台管理系统'
admin.site.site_title = '金饭碗'
admin.site.index_title = '金饭碗后台管理系统'


class DistrictLevel(models.Model):
    level = models.CharField(
        verbose_name=_('辖区等级'), help_text=_('辖区等级'), max_length=100, unique=True, null=True, blank=True)
    datetime_created = models.DateTimeField(verbose_name=_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(verbose_name=_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = _('辖区等级')
        verbose_name_plural = _('辖区等级')

    def __str__(self):
        return '{0}'.format(self.level)


class ChinaDistrict(models.Model):
    city_code = models.CharField(
        verbose_name=_('电话区号'), help_text=_('电话区号'), max_length=100, null=True, blank=True)
    ad_code = models.CharField(verbose_name=_('辖区编号'), help_text=_('辖区编号'), max_length=100, null=True, blank=True)
    name = models.CharField(verbose_name=_('辖区名称'), help_text=_('辖区名称'), max_length=100, null=True, blank=True)
    center = models.CharField(verbose_name=_('中心坐标'), help_text=_('中心坐标'), max_length=100, null=True, blank=True)
    level = models.ForeignKey(
        DistrictLevel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('辖区等级'),
        help_text=_('辖区等级')
    )
    parent_district = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('上级辖区'),
        help_text=_('上级辖区')
    )
    datetime_created = models.DateTimeField(verbose_name=_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(verbose_name=_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = _('中国行政区')
        verbose_name_plural = _('中国行政区')

    def __str__(self):
        return '{0}'.format(self.name)


class UserLevel(models.Model):
    level_code = models.SmallIntegerField(
        verbose_name=_('等级编号'), help_text=_('等级编号'), null=True, unique=True, blank=True)
    level_name = models.CharField(
        verbose_name=_('等级名称'), help_text=_('等级名称'), max_length=100, null=True, unique=True)
    level_desc = models.TextField(
        verbose_name=_('等级描述'), help_text=_('等级描述'), max_length=1000, null=True, blank=True)
    datetime_created = models.DateTimeField(verbose_name=_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(verbose_name=_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = _('用户等级')
        verbose_name_plural = _('用户等级')

    def __str__(self):
        return "{0} {1}".format(
            self.level_code,
            self.level_name,
        )


class Restaurant(models.Model):
    restaurant_name = models.CharField(
        verbose_name=_('餐馆名称'), help_text=_('餐馆名称'), max_length=255, unique=True, null=True, blank=True)
    restaurant_code = models.CharField(
        verbose_name=_('餐馆识别码'), help_text=_('餐馆识别码'), max_length=255, null=True, blank=True)
    contact_person = models.CharField(
        verbose_name=_('联系人'), help_text=_('联系人'), max_length=255, null=True, blank=True)
    contact_mobile = models.CharField(
        verbose_name=_('联系方式'), help_text=_('联系方式'), max_length=255, null=True, blank=True)
    restaurant_address = models.TextField(
        verbose_name=_('餐馆地址'), help_text=_('餐馆地址'), max_length=2000, null=True, blank=True)
    center = models.CharField(
        verbose_name=_('中心坐标'), help_text=_('中心坐标'), max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(
        "WxUser",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='restaurant_created_by',
        verbose_name=_('创建人员'),
        help_text=_('创建人员')
    )
    confirmed_by = models.ForeignKey(
        "WxUser",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='restaurant_confirmed_by',
        verbose_name=_('审核人员'),
        help_text=_('审核人员')
    )
    is_confirmed = models.BooleanField(verbose_name=_('已审核'), help_text=_('已审核'), default=False)
    is_active = models.BooleanField(verbose_name=_('有效'), help_text=_('有效'), default=False)
    datetime_created = models.DateTimeField(verbose_name=_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(verbose_name=_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = _('餐馆')
        verbose_name_plural = _('餐馆')

    def __str__(self):
        return "{0} {1}".format(
            self.restaurant_name,
            self.restaurant_code,
        )


class DishTag(models.Model):
    tag_name = models.CharField(
        verbose_name=_('标签'), help_text=_('标签'), max_length=255, null=True, blank=True, unique=True)
    created_by = models.ForeignKey(
        "WxUser",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='dish_tag_created_by',
        verbose_name=_('创建人员'),
        help_text=_('创建人员'),
    )
    confirmed_by = models.ForeignKey(
        "WxUser",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='dish_tag_confirmed_by',
        verbose_name=_('审核人员'),
        help_text=_('审核人员'),
    )
    is_confirmed = models.BooleanField(verbose_name=_('已审核'), help_text=_('已审核'), default=True)
    is_active = models.BooleanField(verbose_name=_('是否有效'), help_text=_('是否有效'), default=True)
    datetime_created = models.DateTimeField(verbose_name=_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(verbose_name=_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-id']
        verbose_name = _('标签')
        verbose_name_plural = _('标签')

    def __str__(self):
        return "{0}".format(
            self.tag_name,
        )


class Dish(models.Model):
    dish_name = models.CharField(
        verbose_name=_('商品名称'), help_text=_('商品名称'), max_length=255, null=True, blank=True)
    dish_image_0 = models.ImageField(
        verbose_name=_('主照片'), help_text=_('主照片'), upload_to='dish/', null=True, blank=True)
    dish_image_1 = models.ImageField(
        verbose_name=_('照片1'), help_text=_('照片1'), upload_to='dish/', null=True, blank=True)
    dish_image_2 = models.ImageField(
        verbose_name=_('照片2'), help_text=_('照片2'), upload_to='dish/', null=True, blank=True)
    dish_image_3 = models.ImageField(
        verbose_name=_('照片3'), help_text=_('照片3'), upload_to='dish/', null=True, blank=True)
    dish_desc = models.TextField(
        verbose_name=_('菜品描述'), help_text=_('菜品描述'), max_length=2000, null=True, blank=True)
    dish_price = models.DecimalField(
        verbose_name=_('商品价格'), help_text=_('商品价格'), null=True, decimal_places=2, max_digits=9, default=18.00)
    restaurant = models.ForeignKey(
        Restaurant,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('餐馆'),
        help_text=_('餐馆'),
    )
    dish_tag = models.ManyToManyField(
        DishTag,
        blank=True,
        verbose_name=_('标签'),
        help_text=_('标签'),
    )
    is_active = models.BooleanField(verbose_name=_('是否有效'), help_text=_('是否有效'), default=True)
    datetime_created = models.DateTimeField(verbose_name=_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(verbose_name=_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = _('商品')
        verbose_name_plural = _('商品')

    def __str__(self):
        return "{0}".format(
            self.dish_name,
        )


class Company(models.Model):
    """
    公司列表，通常由管理员进行后台添加，游客用户也可以自行创建，由管理员进行审核；
    公司的管理员有权限更新 restaurant 信息，一个公司有多个管理员；
    """
    company_name = models.CharField(
        verbose_name=_('企业名称'), help_text=_('企业名称'), max_length=255, unique=True, null=True, blank=True)
    company_code = models.CharField(
        verbose_name=_('企业识别码'), help_text=_('企业识别码'), max_length=255, unique=True, null=True, blank=True)
    company_address = models.TextField(
        verbose_name=_('企业地址'), help_text=_('企业地址'), max_length=2000, null=True, blank=True)
    center = models.CharField(
        verbose_name=_('中心坐标'), help_text=_('中心坐标'), max_length=255, null=True, blank=True)
    deliver_time_0 = models.TimeField(
        verbose_name=_('早餐送餐时间'), help_text=_('早餐送餐时间'), null=True, default='8:00:00')
    deliver_time_1 = models.TimeField(
        verbose_name=_('午餐送餐时间'), help_text=_('午餐送餐时间'), null=True, default='11:50:00')
    deliver_time_2 = models.TimeField(
        verbose_name=_('下午茶送餐时间'), help_text=_('下午茶送餐时间'), null=True, default='15:00:00')
    deliver_time_3 = models.TimeField(
        verbose_name=_('晚餐送餐时间'), help_text=_('晚餐送餐时间'), null=True, default='17:50:00')
    deliver_time_4 = models.TimeField(
        verbose_name=_('夜宵送餐时间'), help_text=_('夜宵送餐时间'), null=True, default='20:00:00')
    restaurant = models.ManyToManyField(
        Restaurant,
        blank=True,
        verbose_name=_('可见餐馆'),
        help_text=_('可见餐馆'),
        related_name='company_related_restaurant'
    )
    created_by = models.ForeignKey(
        "WxUser",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='company_created_by',
        verbose_name=_('创建人员'),
        help_text=_('创建人员'),
    )
    confirmed_by = models.ForeignKey(
        "WxUser",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='company_confirmed_by',
        verbose_name=_('审核人员'),
        help_text=_('审核人员'),
    )
    is_confirmed = models.BooleanField(verbose_name=_('已审核'), help_text=_('已审核'), default=False)
    is_active = models.BooleanField(verbose_name=_('有效'), help_text=_('有效'), default=False)
    datetime_created = models.DateTimeField(verbose_name=_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(verbose_name=_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = _('企业')
        verbose_name_plural = _('企业')

    def __str__(self):
        return "{0} {1}".format(
            self.company_name,
            self.company_code,
        )


class WxUser(AbstractUser):
    """
    用户列表
    如果用户有 company 关联信息，用户可以进行订餐；
    如果用户有 company 关联信息，并且 is_manager 是 True，用户可以统计公司的订单，审核和管理公司员工名单 CompanyEmployee；
    """
    # 微信同步的用户信息
    openid = models.CharField(
        verbose_name=_('微信OpenID'), help_text=_('微信OpenID'), max_length=100, unique=True, null=True, blank=True)
    avatar_url = models.URLField(
        verbose_name=_('头像'), help_text=_('头像'), null=True, blank=True)
    nick_name = models.CharField(
        verbose_name=_('昵称'), help_text=_('昵称'), max_length=100, null=True, blank=True, unique=True)
    gender = models.SmallIntegerField(
        verbose_name=_('性别'), help_text=_('性别'), choices=((1, '男'), (2, '女'), (0, '未知')), null=True, blank=True)
    language = models.CharField(
        verbose_name=_('语言'), help_text=_('语言'), max_length=100, null=True, blank=True)
    city = models.CharField(
        verbose_name=_('城市'), help_text=_('城市'), max_length=200, null=True, blank=True)
    province = models.CharField(
        verbose_name=_('省份'), help_text=_('省份'), max_length=200, null=True, blank=True)
    country = models.CharField(
        verbose_name=_('国家'), help_text=_('国家'), max_length=200, null=True, blank=True)

    date_of_birth = models.DateField(verbose_name=_('出生日期'), help_text=_('出生日期'), null=True, blank=True)
    desc = models.TextField(verbose_name=_('描述'), help_text=_('描述'), max_length=2000, null=True, blank=True)
    mobile = models.CharField(
        verbose_name=_('手机号'), help_text=_('手机号'), max_length=100, null=True, blank=True, unique=True)
    user_level = models.ForeignKey(
        UserLevel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('用户等级'),
        help_text=_('用户等级'),
    )
    china_district = models.ForeignKey(
        ChinaDistrict,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('所在辖区'),
        help_text=_('所在辖区'),
    )
    company = models.ForeignKey(
        Company,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('公司'),
        help_text=_('公司'),
        related_name='wx_user'
    )
    restaurant = models.ForeignKey(
        Restaurant,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('餐馆'),
        help_text=_('餐馆'),
    )
    current_role = models.IntegerField(
        verbose_name=_('当前用户角色'), help_text=_('当前用户角色'), null=True, default=0, choices=role_choices)
    is_owner = models.BooleanField(verbose_name=_('是商家'), help_text=_('是商家'), default=False)
    is_client = models.BooleanField(verbose_name=_('是客户'), help_text=_('是客户'), default=True)
    is_manager = models.BooleanField(verbose_name=_('是管理员'), help_text=_('是管理员'), default=False)
    datetime_created = models.DateTimeField(verbose_name=_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(verbose_name=_('更新时间'), auto_now=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return "[{0}] {1}".format(
            self.pk,
            self.username,
        )


class CompanyEmployee(models.Model):
    """
    企业员工列表，员工必须在此表内，并且 is_confirmed 和 is_active 同时为 True，才允许进行自行注册通过；
    如果员工没有在此表内，员工可以自行提交，公司管理员进行审核，审核通过以后员工与公司在 WxUser 进行关联；
    """
    company = models.ForeignKey(
        Company,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('公司'),
    )
    employee_name = models.CharField(verbose_name=_('姓名'), help_text=_('姓名'), max_length=200, null=True, blank=True)
    mobile = models.CharField(
        verbose_name=_('手机号'), help_text=_('手机号'), max_length=20, null=True, blank=True, unique=True)
    user = models.ForeignKey(
        WxUser,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='company_employee_user',
        verbose_name=_('用户'),
        help_text=_('用户'),
    )
    created_by = models.ForeignKey(
        WxUser,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='company_employee_created_by',
        verbose_name=_('创建人员'),
        help_text=_('创建人员'),
    )
    confirmed_by = models.ForeignKey(
        WxUser,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='company_employee_confirmed_by',
        verbose_name=_('审核人员'),
        help_text=_('创建人员'),
    )
    is_confirmed = models.BooleanField(verbose_name=_('已审核'), help_text=_('已审核'), default=False)
    is_active = models.BooleanField(verbose_name=_('有效'), help_text=_('有效'), default=False)
    datetime_created = models.DateTimeField(verbose_name=_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(verbose_name=_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
        unique_together = ('company', 'employee_name', 'mobile')
        verbose_name = _('企业员工名单')
        verbose_name_plural = _('企业员工名单')

    def __str__(self):
        return "{0} {1}".format(
            self.employee_name,
            self.mobile,
        )


class Order(models.Model):
    order_code = models.CharField(
        verbose_name=_('订单编号'), help_text=_('订单编号'), max_length=255, unique=True, null=True, blank=True)
    order_date = models.DateField(
        verbose_name=_('订单日期'), help_text=_('订单日期'), null=True, blank=True)
    order_type = models.IntegerField(
        verbose_name=_('订餐类型'),
        help_text=_("订餐类型 (0-->早餐, 1-->午餐, 2-->下午茶, 3-->晚餐, 4-->夜宵, 5-->其他)"),
        null=True, default=1,
        choices=[(0, '早餐'), (1, '午餐'), (2, '下午茶'), (3, '晚餐'), (4, '夜宵'), (5, '其他')]
    )
    deliver_time = models.TimeField(
        verbose_name=_('送餐时间'), help_text=_('送餐时间'), null=True, blank=True
    )
    total_marked_price = models.DecimalField(
        verbose_name=_('订单标价'), help_text=_('订单标价'), null=True, blank=True, decimal_places=2, max_digits=9)
    total_discount = models.DecimalField(
        verbose_name=_('订单折扣'), help_text=_('订单折扣'), null=True, blank=True, decimal_places=2, max_digits=9)
    total_price = models.DecimalField(
        verbose_name=_('订单金额'), help_text=_('订单金额'), null=True, blank=True, decimal_places=2, max_digits=9)
    item_count = models.IntegerField(
        verbose_name=_('产品数量'), help_text=_('产品数量'), null=True, blank=True)
    restaurant = models.ForeignKey(
        Restaurant,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('餐馆'),
        help_text=_('餐馆'),
    )
    client = models.ForeignKey(
        WxUser,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('用户'),
        help_text=_('用户'),
    )
    is_submitted = models.BooleanField(verbose_name=_('已经提交'), help_text=_('已经提交'), default=False)
    is_payed = models.BooleanField(verbose_name=_('已经支付'), help_text=_('已经支付'), default=False)
    is_active = models.BooleanField(verbose_name=_('是否有效'), help_text=_('是否有效'), default=True)
    datetime_created = models.DateTimeField(verbose_name=_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(verbose_name=_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = _('订单')
        verbose_name_plural = _('订单')

    def __str__(self):
        return "{0}".format(
            self.order_code
        )


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('订单'), help_text=_('订单'),
    )
    dish = models.ForeignKey(
        Dish,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('商品'), help_text=_('商品'),
    )
    item_count = models.IntegerField(verbose_name=_('数量'), help_text=_('数量'), null=True, blank=True)
    marked_price = models.DecimalField(
        verbose_name=_('标价'), help_text=_('标价'), null=True, blank=True, decimal_places=2, max_digits=9)
    payed_unit_price = models.DecimalField(
        verbose_name=_('单价'), help_text=_('单价'), null=True, blank=True, decimal_places=2, max_digits=9)
    payed_total_price = models.DecimalField(
        verbose_name=_('小计'), help_text=_('小计'), null=True, blank=True, decimal_places=2, max_digits=9)
    is_active = models.BooleanField(verbose_name=_('是否有效'), help_text=_('是否有效'), default=True)
    datetime_created = models.DateTimeField(verbose_name=_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(verbose_name=_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = _('订单明细')
        verbose_name_plural = _('订单明细')

    def __str__(self):
        return "{0} {1}".format(
            self.order,
            self.dish
        )
