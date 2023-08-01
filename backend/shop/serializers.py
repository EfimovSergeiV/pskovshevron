from rest_framework import serializers
from shop.models import (
    CategoryModel,
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


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализация товаров """
    
    product_images = ImageProductSerializer( many=True )
    product_properties = ProductPropertySerializer( many=True )

    class Meta:
        model = ProductModel
        fields = ( 'id', 'title', 'description', 'wildberries', 'price', 'product_images', 'product_properties','category' )