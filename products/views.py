from rest_framework import generics
from .models import Product
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrReadOnly


class ProductsListAPIView(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):


        queryset = Product.objects.all()
        category = self.kwargs.get('category')

        if category:
            queryset = queryset.filter(category=category)

        return queryset
    
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        
        serializer.save(product_owner=self.request.user)

    



class ProductDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def destroy(self, request, *args, **kwargs):
    #     print("estoy borrando")
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     print(f"Product {instance.id} has been deleted.")
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class MyProductsAPIView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = ProductSerializer

    def get_queryset(self):

        queryset = Product.objects.all().filter(product_owner=self.request.user)
        return queryset

