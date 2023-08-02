from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FileUploadParser

from shop.models import ProductModel, CategoryModel, OrderModel
from shop.serializers import ProductSerializer, CategorySerializer, OrderSerializer



class MainPageView(APIView):
    """    Главная страница API """
    def get(self, request):
        html = "<html><body><h1> API PSKOVSHEVRON.RU</h1><br /><a href='http://127.0.0.1:8000/admin/'> Перейти в админ панель</body></html>"
        return HttpResponse(html)


class ProductsPagination(PageNumberPagination):
    """ Ограничение пагинации """
    page_size = 36


class CategoriesView(APIView):

    def get(self, request):
        categories_qs = CategoryModel.objects.all()
        serializer = CategorySerializer( categories_qs, many=True, context={'request':request} )

        return Response(serializer.data)


class ListProductsView(ListAPIView):
    """ Список товаров """

    serializer_class = ProductSerializer
    pagination_class = ProductsPagination
    qs = ProductModel.objects.filter(activated=True)

    def get_queryset(self, *args, **kwargs):
        props = dict(self.request.query_params)
        if 'ct' in props.keys():
            products_qs = self.qs.filter(category__in=props['ct'])
        else:
            products_qs = self.qs
        
        return products_qs
    

class ProductView(APIView):

    def get(self, request, pk):

        product_qs = ProductModel.objects.get( id=pk )
        serializer = ProductSerializer( product_qs, context={'request':request} )

        return Response(serializer.data)
    

class OrderView(APIView):
    """ Обработка заказов """

    def post(self, request):
        
        filename = False
        if "image_for_custom" in request.FILES.keys():
            fs = FileSystemStorage()
            filename = fs.save(f'order/images/{request.FILES["image_for_custom"].name}', request.FILES["image_for_custom"])

        order_products = []

        if 'products' in request.data.keys():
            products_qs = ProductModel.objects.filter(id__in=[product['id'] for product in request.data['products'] ])
            for product in request.data['products']:
                order_products.append({
                    "prod_id": product['id'],
                    "image": product['product_images'][0]['image'],
                    "title": product['title'],
                    "price": products_qs.get(id=product['id']).price, #   Защита от подмены стоимости
                    "quantity": product['quantity'],
                })

        data = {
            'client_name': request.data['name'],
            'contact_data': request.data['contact'],
            'order_products': order_products
        }

        serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            order = serializer.save()
            if filename:
                OrderModel.objects.filter(id=order.id).update(image_for_custom=filename)

            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)