from django.urls import path, include
from .views import *

urlpatterns = [
    path('info/',infoList.as_view()),
    path('products/',ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('category/<str:category>/',ProductCategoryList.as_view()),
    path('category/',CategoryList.as_view()),
    path('product-variations/<int:productID>/',ProductVariationList.as_view()),
]