from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    # product_owner = UserOwnerSerializer(read_only=True)
    product_owner = serializers.ReadOnlyField(source='product_owner.username')

    class Meta:
        model = Product
        fields = ["id", "product_name", "product_description", "category", "price", "product_image", "product_owner"]



