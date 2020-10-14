from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    created_date = serializers.DateTimeField()
    modified_date = serializers.DateTimeField()
