from rest_framework import serializers
from product.models import *


class RecursiveCategorySerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = CategorySerializer(value, context=self.context)
        return serializer.data
class CategorySerializer(serializers.ModelSerializer):
  parent = RecursiveCategorySerializer()
  class Meta:
    model = Category
    fields = ('id',
              'name',
              'slug',
              'parent')

class ProductSerializer(serializers.ModelSerializer):

  category = CategorySerializer(read_only=True)
  class Meta:
    model = Product
    fields = '__all__'
