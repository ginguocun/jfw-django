from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class DistrictLevel(models.Model):
    level = models.CharField(_('辖区等级'), max_length=100, unique=True, null=True, blank=True)
    datetime_created = models.DateTimeField(_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = _('辖区等级')
        verbose_name_plural = _('辖区等级')

    def __str__(self):
        return '{0}'.format(self.level)


class ChinaDistrict(models.Model):
    city_code = models.CharField(_('电话区号'), max_length=100, null=True, blank=True)
    ad_code = models.CharField(_('辖区编号'), max_length=100, null=True, blank=True)
    name = models.CharField(_('辖区名称'), max_length=100, null=True, blank=True)
    center = models.CharField(_('中心坐标'), max_length=100, null=True, blank=True)
    level = models.ForeignKey(
        DistrictLevel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('辖区等级')
    )
    parent_district = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('上级辖区')
    )
    datetime_created = models.DateTimeField(_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = _('中国行政区')
        verbose_name_plural = _('中国行政区')

    def __str__(self):
        return '{0}'.format(self.name)


class UserLevel(models.Model):
    level_code = models.SmallIntegerField(_('等级编号'), null=True, unique=True, blank=True)
    level_name = models.CharField(_('等级名称'), max_length=100, null=True, unique=True)
    level_desc = models.TextField(_('等级描述'), max_length=1000, null=True, blank=True)
    datetime_created = models.DateTimeField(_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('更新时间'), auto_now=True)

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
    restaurant_name = models.CharField(_('餐馆名称'), max_length=255, unique=True, null=True, blank=True)
    restaurant_code = models.CharField(_('餐馆企业识别码'), max_length=255, null=True, blank=True)
    restaurant_address = models.TextField(_('餐馆地址'), max_length=2000, null=True, blank=True)
    center = models.CharField(_('中心坐标'), max_length=255, null=True, blank=True)
    is_available = models.BooleanField(_('是否有效'), default=True)
    datetime_created = models.DateTimeField(_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('更新时间'), auto_now=True)

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


class Dish(models.Model):
    dish_name = models.CharField(_('菜品名称'), max_length=255, null=True, blank=True)
    dish_image_0 = models.ImageField(_('主照片'), upload_to='dish/', null=True, blank=True)
    dish_image_1 = models.ImageField(_('照片1'), upload_to='dish/', null=True, blank=True)
    dish_image_2 = models.ImageField(_('照片2'), upload_to='dish/', null=True, blank=True)
    dish_image_3 = models.ImageField(_('照片3'), upload_to='dish/', null=True, blank=True)
    dish_desc = models.TextField(_('菜品描述'), max_length=2000, null=True, blank=True)
    dish_price = models.DecimalField(_('菜品价格'), null=True, decimal_places=2, max_digits=9, default=18.00)
    is_available = models.BooleanField(_('是否有效'), default=True)
    restaurant = models.ForeignKey(
        Restaurant,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('餐馆')
    )
    datetime_created = models.DateTimeField(_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = _('菜品')
        verbose_name_plural = _('菜品')

    def __str__(self):
        return "{0}".format(
            self.dish_name,
        )


class Company(models.Model):
    company_name = models.CharField(_('企业名称'), max_length=255, unique=True, null=True, blank=True)
    company_code = models.CharField(_('企业识别码'), max_length=255, unique=True, null=True, blank=True)
    company_address = models.TextField(_('企业地址'), max_length=2000, null=True, blank=True)
    center = models.CharField(_('中心坐标'), max_length=255, null=True, blank=True)
    is_available = models.BooleanField(_('是否有效'), default=True)
    restaurant = models.ManyToManyField(
        Restaurant,
        blank=True,
        verbose_name=_('可见餐馆')
    )
    datetime_created = models.DateTimeField(_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('更新时间'), auto_now=True)

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

    openid = models.CharField(_('微信OpenID'), max_length=100, unique=True, null=True, blank=True)
    avatar_url = models.URLField(_('头像'), null=True, blank=True)
    nick_name = models.CharField(_('昵称'), max_length=100, null=True, blank=True, unique=True)
    gender = models.SmallIntegerField(_('性别'), choices=((1, '男'), (2, '女'), (0, '未知')), null=True, blank=True)
    language = models.CharField(_('语言'), max_length=100, null=True, blank=True)
    city = models.CharField(_('城市'), max_length=200, null=True, blank=True)
    province = models.CharField(_('省份'), max_length=200, null=True, blank=True)
    country = models.CharField(_('国家'), max_length=200, null=True, blank=True)
    date_of_birth = models.DateField(_('出生日期'), null=True, blank=True)

    desc = models.TextField(_('描述'), max_length=2000, null=True, blank=True)
    mobile = models.CharField(_('手机号'), max_length=100, null=True, blank=True, unique=True)
    user_level = models.ForeignKey(
        UserLevel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('用户等级'),
    )
    china_district = models.ForeignKey(
        ChinaDistrict,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('所在辖区')
    )
    company = models.ForeignKey(
        Company,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('公司')
    )
    restaurant = models.ForeignKey(
        Restaurant,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('餐馆')
    )
    is_owner = models.BooleanField(_('是商家'), default=False, null=True)
    is_client = models.BooleanField(_('是客户'), default=True, null=True)
    is_manager = models.BooleanField(_('是管理员'), default=True, null=True)
    datetime_created = models.DateTimeField(_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('更新时间'), auto_now=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return "[{0}] {1}".format(
            self.pk,
            self.nick_name,
        )


class Order(models.Model):
    order_code = models.CharField(_('订单编号'), max_length=255, unique=True, null=True, blank=True)
    order_date = models.DateField(_('订单日期'), null=True, blank=True)
    total_marked_price = models.DecimalField(_('订单标价'), null=True, blank=True, decimal_places=2, max_digits=9)
    total_discount = models.DecimalField(_('订单折扣'), null=True, blank=True, decimal_places=2, max_digits=9)
    total_price = models.DecimalField(_('订单金额'), null=True, blank=True, decimal_places=2, max_digits=9)
    item_count = models.IntegerField(_('产品数量'), null=True, blank=True)
    restaurant = models.ForeignKey(
        Restaurant,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('餐馆')
    )
    client = models.ForeignKey(
        WxUser,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('用户')
    )
    is_payed = models.BooleanField(_('已经支付'), default=False)
    is_available = models.BooleanField(_('是否有效'), default=True)
    datetime_created = models.DateTimeField(_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('更新时间'), auto_now=True)

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
        verbose_name=_('订单')
    )
    dish = models.ForeignKey(
        Dish,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('产品')
    )
    item_count = models.IntegerField(_('数量'), null=True, blank=True)
    marked_price = models.DecimalField(_('标价'), null=True, blank=True, decimal_places=2, max_digits=9)
    payed_unit_price = models.DecimalField(_('单价'), null=True, blank=True, decimal_places=2, max_digits=9)
    payed_total_price = models.DecimalField(_('小计'), null=True, blank=True, decimal_places=2, max_digits=9)
    is_available = models.BooleanField(_('是否有效'), default=True)
    datetime_created = models.DateTimeField(_('记录时间'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('更新时间'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = _('订单')
        verbose_name_plural = _('订单')

    def __str__(self):
        return "{0} {1}".format(
            self.order,
            self.dish
        )
