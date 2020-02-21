from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *


class JfwTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(JfwTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = 'wx_{0}'.format(user.username)
        return token


class WxUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = WxUser
        fields = ['id', 'nick_name', 'avatar_url', 'gender', 'is_owner', 'is_client', 'is_manager']


class RestaurantListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'


class DishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = '__all__'


class CompanyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'

