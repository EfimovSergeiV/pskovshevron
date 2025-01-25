from rest_framework import serializers
from main.models import ContactsModel


class ProductPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsModel
        fields = '__all__'
