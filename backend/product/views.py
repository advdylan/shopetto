from django.shortcuts import render
from product.models import *
from product.serializers import *
from rest_framework import generics, status, permissions, viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .permissions import ReadOnlyOrAuthenticated
# Create your views here.

import json

class ProductViewSet(viewsets.ModelViewSet):

  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [ReadOnlyOrAuthenticated]

