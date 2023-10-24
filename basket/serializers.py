from rest_framework import serializers
from .models import Basket

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ['id','name','description', 'image_url']