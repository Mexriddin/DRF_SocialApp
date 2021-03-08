from rest_framework import serializers
from .models import Partner, Category, SocialNetwork

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class SocialNetworkSerializer(serializers.ModelSerializer):
    partner = PartnerSerializer()
    category = CategorySerializer()
    class Meta:
        model = SocialNetwork
        fields = '__all__'
