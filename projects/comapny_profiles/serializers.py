from rest_framework import serializers
from .models import Postion, company


class postionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postion
        fields = '__all__'


class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = '__all__'
