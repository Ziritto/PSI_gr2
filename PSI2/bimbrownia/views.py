
from .serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class Clientlist(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['first_name','last_name','gender','address']
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']

class ClientDetale(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['first_name','last_name','gender','address']
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']

class alcohollist(generics.ListCreateAPIView):
    queryset = alcohol.objects.all()
    serializer_class = alcoholSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name','alcohol_category','taste','how_strong']
    search_fields = ['name', 'alcohol_category']
    ordering_fields = ['name', 'alcohol_category']

class alcoholDetale(generics.RetrieveUpdateDestroyAPIView):
    queryset = alcohol.objects.all()
    serializer_class = alcoholSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name','alcohol_category','taste','how_strong']
    search_fields = ['name', 'alcohol_category']
    ordering_fields = ['name', 'alcohol_category']

class alcoholCategorylist(generics.ListCreateAPIView):
    queryset = alcoholCategory.objects.all()
    serializer_class = alcoholCategorySerializer

class alcoholCategoryDetale(generics.RetrieveUpdateDestroyAPIView):
    queryset = alcoholCategory.objects.all()
    serializer_class = alcoholCategorySerializer

class Orderlist(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['client','alcohol','price']
    search_fields = ['client', 'price']
    ordering_fields = ['client', 'price']

class OrderDetale(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['client','alcohol','price']
    search_fields = ['client', 'price']
    ordering_fields = ['client', 'price']





