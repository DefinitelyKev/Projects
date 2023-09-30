from .models import Product
from rest_framework import serializers


class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        return obj.get_discount()
