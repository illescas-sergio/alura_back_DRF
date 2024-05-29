from django.urls import path
from .views import ProductsListAPIView, ProductDetailsAPIView, MyProductsAPIView

urlpatterns = [
    path('', ProductsListAPIView.as_view(), name="products_view"),
    path('category/<str:category>/', ProductsListAPIView.as_view(), name='products_category_view'),
    path('user/my_products/', MyProductsAPIView.as_view(), name='my_products'),
    path('<uuid:pk>/', ProductDetailsAPIView.as_view(), name='products_detail_view'),
]