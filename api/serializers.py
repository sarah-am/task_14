from restaurants.models import Restaurant
from rest_framework import serializers


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'opening_time', 'closing_time',]