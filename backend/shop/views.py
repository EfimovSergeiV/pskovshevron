from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from shop.models import ProductModel, CategoryModel
from shop.serializers import ProductSerializer, CategorySerializer



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