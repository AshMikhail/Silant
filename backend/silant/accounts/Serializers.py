from rest_framework import serializers
from . import models


class baseCompanySerializer(serializers.Serializer):
    id = serializers.CharField()
    id_user = serializers.CharField(source='user.id', max_length=200)
    user = serializers.CharField(source='user.username', max_length=200)
    name = serializers.CharField()
    сategory = serializers.CharField()

    class Meta:
        fields = ['id', 'id_user', 'user', 'сategory']

class serviceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.service_company
        fields = '__all__'

class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.client
        fields = '__all__'
