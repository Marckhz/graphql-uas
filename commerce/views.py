from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework import viewsets

from rest_framework import generics


from rest_framework.pagination import PageNumberPagination

from .models import Shop


from .serializers import ShopSerializer
# Create your views here.

@api_view(['GET'])
def say_hello(request):
    return Response({"data":"Hello World"})


class HelloWorld(APIView):
    '''returns a simple hello world'''

    def get(self, request):
        return Response({"data":"Hello World"})


class ShopViewSet(viewsets.ModelViewSet):
    
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    paginatin_class = PageNumberPagination


