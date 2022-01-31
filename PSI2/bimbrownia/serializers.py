from rest_framework import serializers
from .models import alcoholCategory, alcohol, Client, Order
import re

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name',
                  'gender', 'address']


class alcoholCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = alcoholCategory
        fields = ['id', 'name']

class alcoholSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = alcohol
        fields = ['id', 'name', 'taste', 'how_strong']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'price']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Don't make price lower or equal to zero", )
        return value


