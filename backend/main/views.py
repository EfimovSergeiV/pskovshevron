from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FileUploadParser

from main.models import ContactsModel
from main.serializers import ProductPropertySerializer


class ContactsView(APIView):
    def get(self, request):
        contacts = ContactsModel.objects.first()
        serializer = ProductPropertySerializer(contacts)
        return Response(serializer.data)
