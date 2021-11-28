from .models import Discount, DiscountType, Store
from rest_framework import serializers


class DiscountSerializers(serializers.ModelSerializer):
    class Meta:
        model= Discount
        fields = ['create_date', 'end_date', 'code', 'store', 'status']
        read_only_fields = ['create_date', 'end_date', 'code', 'store', 'status']
