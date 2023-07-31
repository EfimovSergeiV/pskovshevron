from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from shop.models import ProductModel
from shop.serializers import ProductSerializer



class MainPageView(APIView):
    """    Главная страница API """
    def get(self, request):
        html = "<html><body><h1> API PSKOVSHEVRON.RU</h1><br /><a href='http://127.0.0.1:8000/admin/'> Перейти в админ панель</body></html>"
        return HttpResponse(html)


class ProductsPagination(PageNumberPagination):
    """ Ограничение пагинации """
    page_size = 36


class ListProductsView(ListAPIView):
    """ Список товаров """

    serializer_class = ProductSerializer
    pagination_class = ProductsPagination

    def get_queryset(self, *args, **kwargs):
        products_qs = ProductModel.objects.filter(activated=True)
        
        return products_qs
    

class ProductView(APIView):

    def get(self, request, pk):
        print(pk)
        product_qs = ProductModel.objects.get( id=pk )
        serializer = ProductSerializer( product_qs, context={'request':request} )

        return Response(serializer.data)