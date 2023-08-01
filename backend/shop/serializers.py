from rest_framework import serializers
from shop.models import (
    CategoryModel,
    ProductModel,
    ImageProductModel,
    ProductPropertyModel,
    OrderModel,
    OrderProductModel,
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



class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProductModel
        fields = ('prod_id','image','title','price','quantity')


class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer( many=True )

    class Meta:
        model = OrderModel
        fields = ( 'client_name', 'contact_data', 'order_products')


    def create(self, validated_data):
        order_products = validated_data.pop('order_products')
        print('\n\n\FFF',order_products)
        order = OrderModel.objects.create(**validated_data)
        for product in order_products:
            OrderProductModel.objects.create(order = order, **product)
        return order