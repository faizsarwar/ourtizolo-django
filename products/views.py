from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework import status

# Create your views here.


class infoList(APIView):
    def get(self,request,format=None):
        Info=info.objects.all()
        serializer=infoSerializer(Info,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
            serializer=infoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status.HTTP_201_CREATED)
            return Response(status.HTTP_400_BAD_REQUEST)


class ProductList(APIView):
    def get(self,request,format=None):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)

class CategoryList(APIView):
    def get(self,request,format=None):
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get(self, request, pk,format=None):
        product = Product.objects.all().filter(id=pk)
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)    
        
class ProductCategoryList(APIView):
    def get(self, request, category,format=None):
        category = Category.objects.values().get(name_without_space=category)  #fetching category to show products
        product = Product.objects.all().filter(category=category['id'])
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)    
        
class ProductVariationList(APIView):
    def get(self, request, productID,format=None):
        product = Product.objects.values().get(id=productID)
        variation = ProductVariation.objects.all().filter(Product=product['id'])
        serializer = ProductVariationSerializer(variation,many=True)
        return Response(serializer.data)    
