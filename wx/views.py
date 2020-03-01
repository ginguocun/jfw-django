import json
import logging

from django.forms import model_to_dict
from django_filters import rest_framework as filters

from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView

from weixin import WXAPPAPI
from weixin.oauth2 import OAuth2AuthExchangeError

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


def create_or_update_user_info(openid, user_info):
    if openid:
        if user_info:
            user, created = WxUser.objects.update_or_create(openid=openid, defaults=user_info)
        else:
            user, created = WxUser.objects.get_or_create(openid=openid)
        return user
    return None


@api_view(["GET"])
def api_root(request):
    urls = {'method': request.method, 'admin': '/admin/', 'api': '/api/'}
    return Response(urls)


class WxLoginView(APIView):
    """
    post:
    微信登录接口
    """
    authentication_classes = []
    permission_classes = []
    fields = {
        'nick_name': 'nickName',
        'gender': 'gender',
        'language': 'language',
        'city': 'city',
        'province': 'province',
        'country': 'country',
        'avatar_url': 'avatarUrl',
    }

    def post(self, request):
        token = ''
        user_info = dict()
        code = request.data.get('code')
        logger.info("Code: {0}".format(code))
        user_info_raw = request.data.get('user_info', {})
        if isinstance(user_info_raw, str):
            user_info_raw = json.loads(user_info_raw)
        logger.info("user_info: {0}".format(user_info_raw))
        if code:
            api = WXAPPAPI(appid=settings.WX_APP_ID, app_secret=settings.WX_APP_SECRET)
            try:
                session_info = api.exchange_code_for_session_key(code=code)
            except OAuth2AuthExchangeError:
                session_info = None
            if session_info:
                openid = session_info.get('openid', None)
                if openid:
                    if user_info_raw:
                        for k, v in self.fields.items():
                            user_info[k] = user_info_raw.get(v)
                    user = create_or_update_user_info(openid, user_info)
                    if user:
                        token = JfwTokenObtainPairSerializer.get_token(user).access_token
                        return Response(
                            {
                                'jwt': str(token),
                                'user': model_to_dict(
                                    user,
                                    fields=[
                                        'company', 'restaurant', 'current_role',
                                        'is_owner', 'is_client', 'is_manager'
                                    ])
                            },
                            status=HTTP_200_OK)
        return Response({'jwt': str(token), 'user': {}}, status=HTTP_204_NO_CONTENT)


class JfwTokenObtainPairView(TokenObtainPairView):
    """
    Token Obtain API
    """
    serializer_class = JfwTokenObtainPairSerializer


class RestaurantListView(ListCreateAPIView):
    """
    get:
    获取餐馆列表

    post:
    创建餐馆
    """
    queryset = Restaurant.objects.filter(is_active=True)
    serializer_class = RestaurantListSerializer
    search_fields = ('restaurant_name', 'restaurant_code')


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
    search_fields = ['tag_name']
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
    search_fields = ['dish_name', 'dish_desc']
    filterset_class = DishListFilter

    def get_queryset(self):
        if self.request.user.id:
            queryset = self.queryset.filter(
                restaurant__company_related_restaurant__wx_user__id=self.request.user.id
            )
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
    search_fields = ['company_name', 'company_code', 'company_address']
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
    search_fields = ['employee_name', 'mobile_index']
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
    """
    get:
    获取订单详情列表

    post:
    创建订单详情
    """
    queryset = OrderItem.objects.filter(is_active=True)
    serializer_class = OrderItemListSerializer
    filterset_class = OrderItemListFilter
    search_fields = ['dish__title', 'order_code']
