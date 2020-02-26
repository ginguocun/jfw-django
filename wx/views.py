import binascii
import hashlib
import json
import logging

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from django_filters import rest_framework as filters

from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import *

from rest_framework_simplejwt.views import TokenObtainPairView

from weixin import WXAPPAPI

from .serializers import *


logger = logging.getLogger('django')


class WxFilter(filters.FilterSet):

    @classmethod
    def filter_for_field(cls, field, field_name, lookup_expr='exact'):
        filter_class = super().filter_for_field(field, field_name, lookup_expr)
        if lookup_expr == 'exact':
            filter_class.extra['help_text'] = '{0} 等于'.format(field.verbose_name)
        elif lookup_expr == 'contains':
            filter_class.extra['help_text'] = '{0} 包含'.format(field.verbose_name)
        elif lookup_expr == 'gte':
            filter_class.extra['help_text'] = '{0} 大于等于'.format(field.verbose_name)
        elif lookup_expr == 'gt':
            filter_class.extra['help_text'] = '{0} 大于'.format(field.verbose_name)
        elif lookup_expr == 'lt':
            filter_class.extra['help_text'] = '{0} 小于'.format(field.verbose_name)
        elif lookup_expr == 'lte':
            filter_class.extra['help_text'] = '{0} 小于等于'.format(field.verbose_name)
        return filter_class


def make_user_info(openid=None):
    key = settings.SECRET_KEY
    if openid:
        username = hashlib.pbkdf2_hmac("sha256", openid.encode(encoding='utf-8'), key.encode(encoding='utf-8'), 10)
        password = hashlib.pbkdf2_hmac("sha256", username, openid.encode(encoding='utf-8'), 10)
        return {'username': binascii.hexlify(username).decode(), 'password': binascii.hexlify(password).decode()}


def create_user_by_openid(openid=None):
    if openid:
        user_info = make_user_info(openid=openid)
        account = WxUser.objects.create(openid=openid, **user_info)
        return account
    return None


@api_view(["GET"])
def api_root(request):
    urls = {'admin': '/admin/', 'api': '/api/'}
    return Response(urls)


@csrf_exempt
@api_view(["GET", "POST"])
def wx_login(request):
    if request.method == "POST":
        if request.body:
            received_data = json.loads(request.body.decode('utf-8'))
            code = received_data.get('code', None)
            logger.info("Code: {0}".format(code))
            user_info = received_data.get('user_info', None)
            logger.info("user_info: {0}".format(user_info))
            if code:
                api = WXAPPAPI(appid=settings.WX_APP_ID, app_secret=settings.WX_APP_SECRET)
                try:
                    session_info = api.exchange_code_for_session_key(code=code)
                    openid = session_info.get('openid', None)
                    if openid:
                        queryset = WxUser.objects.filter(openid=openid)
                        if queryset.exists():
                            account = queryset.first()
                        else:
                            account = create_user_by_openid(openid=openid)
                        if account:
                            if user_info:
                                account.nick_name = user_info['nickName']
                                account.gender = user_info['gender']
                                account.language = user_info['language']
                                account.city = user_info['city']
                                account.province = user_info['province']
                                account.country = user_info['country']
                                account.avatar_url = user_info['avatarUrl']
                                account.save()
                                logger.info("Account saved: pk={0}".format(account.pk))
                            token = JfwTokenObtainPairSerializer.get_token(account).access_token
                            is_sync = False
                            if account.nick_name:
                                is_sync = True
                            return Response({'jwt': str(token), 'is_sync': is_sync}, status=HTTP_200_OK)
                        return Response({'err': '数据库连接失败'}, status=HTTP_500_INTERNAL_SERVER_ERROR)
                    return Response({'err': '提供的数据验证失败'}, status=HTTP_400_BAD_REQUEST)
                except Exception as err:
                    return Response({'err': str(err)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'err': '访问方式不对'}, status=HTTP_400_BAD_REQUEST)


class JfwTokenObtainPairView(TokenObtainPairView):
    """
    Token Obtain API
    """
    serializer_class = JfwTokenObtainPairSerializer


class RestaurantListView(ListCreateAPIView):
    queryset = Restaurant.objects.filter(is_active=True)
    serializer_class = RestaurantListSerializer
    search_fields = (
        'restaurant_name', 'restaurant_code'
    )


class DishTagListFilter(WxFilter):

    class Meta:
        model = DishTag
        fields = {
            'tag_name': ['exact', 'contains'],
            'is_confirmed': ['exact', 'contains'],
            'is_active': ['exact', 'contains'],
        }


class DishTagListView(ListCreateAPIView):
    """
    get:
    获取商品标签列表

    post:
    创建商品标签
    """
    queryset = DishTag.objects.filter(is_active=True).all()
    serializer_class = DishTagListSerializer
    search_fields = [
        'tag_name'
    ]
    filterset_class = DishTagListFilter


class DishListFilter(WxFilter):

    class Meta:
        model = Dish
        fields = {
            'dish_tag': ['exact'],
            'restaurant': ['exact'],
        }


class DishListView(ListCreateAPIView):
    """
    get:
    获取商品列表

    post:
    创建商品
    """
    permission_classes = []
    queryset = Dish.objects.filter(is_active=True).all()
    serializer_class = DishListSerializer
    search_fields = [
        'dish_name', 'dish_desc'
    ]
    filterset_class = DishListFilter

    def get_queryset(self):
        if self.request.user.id:
            queryset = self.queryset.filter(restaurant__company_related_restaurant__wx_user__id=self.request.user.id)
        else:
            queryset = self.queryset.order_by('-pk')
        return queryset


class CompanyListFilter(WxFilter):

    class Meta:
        model = Company
        fields = {
            'company_name': ['exact', 'contains'],
            'company_code': ['exact', 'contains'],
            'company_address': ['contains'],
        }


class CompanyListView(ListCreateAPIView):
    """
    get:
    获取公司列表

    post:
    创建公司
    """
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanyListSerializer
    search_fields = (
        'company_name', 'company_code', 'company_address'
    )
    filterset_class = CompanyListFilter


class CompanyEmployeeListFilter(WxFilter):

    class Meta:
        model = CompanyEmployee
        fields = {
            'company': ['exact'],
            'employee_name': ['exact', 'contains'],
            'mobile_index': ['exact'],
        }


class CompanyEmployeeListView(ListCreateAPIView):
    """
    get:
    获取企业员工列表

    post:
    创建企业员工
    """
    queryset = CompanyEmployee.objects.filter(is_active=True)
    serializer_class = CompanyEmployeeListSerializer
    search_fields = (
        'employee_name', 'mobile_index',
    )
    filterset_class = CompanyEmployeeListFilter


class OrderListFilter(WxFilter):

    class Meta:
        model = Order
        fields = {
            'client': ['exact'],
            'restaurant': ['exact'],
            'order_date': ['exact']
        }


class OrderListView(ListCreateAPIView):
    """
    get:
    获取订单列表

    post:
    创建订单
    """
    queryset = Order.objects.filter(is_active=True)
    serializer_class = OrderListSerializer
    filterset_class = OrderListFilter


class OrderItemListFilter(WxFilter):

    class Meta:
        model = OrderItem
        fields = {
            'order': ['exact'],
            'dish': ['exact'],
            'dish__title': ['exact', 'contains']
        }


class OrderItemListView(ListCreateAPIView):
    queryset = OrderItem.objects.filter(is_active=True)
    serializer_class = OrderItemListSerializer
    filterset_class = OrderItemListFilter
    search_fields = (
        'dish__title', 'order_code'
    )
