from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# , ListAPIView,
#  RetrieveUpdateAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from testapp.serializers import ProductSerializer,Product
from testapp.pagination import CustomPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
class DetailView(ListCreateAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    #pagination_class=CustomPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class Details_View1(RetrieveUpdateDestroyAPIView):
        serializer_class=ProductSerializer
        queryset=Product.objects.all()
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticatedOrReadOnly]
        