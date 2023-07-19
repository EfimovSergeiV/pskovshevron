from rest_framework import serializers
from shop.models import (
    ProductModel,
    ImageProductModel,
    ProductPropertyModel,
    OrderModel,
)



class ProductPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPropertyModel
        fields = ( 'id', 'name', 'value', )


class ImageProductSerializer(serializers.ModelSerializer):
    """ Сериализация изображений товаров """

    class Meta:
        model = ImageProductModel
        fields = ( 'id', 'image', )


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализация товаров """
    
    product_image = ImageProductSerializer( many=True )
    product_property = ProductPropertySerializer( many=True )

    class Meta:
        model = ProductModel
        fields = ( '__all__' )