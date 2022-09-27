from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

# Create your views here.
class TestemonialList(APIView):
    def get(self,request,format=None):
        products=Testemonial.objects.all()
        serializer=TestemonialSerializer(products,many=True)
        return Response(serializer.data)

# Create your views here.
class FaqList(APIView):
    def get(self,request,format=None):
        products=Faq.objects.all()
        serializer=FaqSerializer(products,many=True)
        return Response(serializer.data)

# Create your views here.
class BlogList(APIView):
    def get(self,request,format=None):
        products=Blog.objects.all()
        serializer=BlogSerializer(products,many=True)
        return Response(serializer.data)

# Create your views here.
class PressList(APIView):
    def get(self,request,format=None):
        products=Press.objects.all()
        serializer=PressSerializer(products,many=True)
        return Response(serializer.data)

# Create your views here.
class ResearchList(APIView):
    def get(self,request,format=None):
        research=Research.objects.all()
        serializer=ResearchSerializer(research,many=True)
        return Response(serializer.data)

class ResearchDetail(APIView):
    def get(self, request, pk,format=None):
        research=Research.objects.all().filter(id=pk)
        serializer = ResearchSerializer(research,many=True)
        return Response(serializer.data)

class BlogDetail(APIView):
    def get(self, request, pk,format=None):
        blog=Blog.objects.all().filter(id=pk)
        serializer = BlogSerializer(blog,many=True)
        return Response(serializer.data)

class PressDetail(APIView):
    def get(self, request, pk,format=None):
        press=Blog.objects.all().filter(id=pk)
        serializer = BlogSerializer(press,many=True)
        return Response(serializer.data)