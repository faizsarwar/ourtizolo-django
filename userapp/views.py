from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from django.http import Http404
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status, authentication, permissions

# Create your views here.
class UserList(APIView):
    def get(self,request,format=None):
            user=User.objects.all()
            serializer=UserCreateSerializer(user,many=True)
            return Response(serializer.data)

    def post(self,request,format=None):
            print(request.data)
            serializer=UserCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status.HTTP_201_CREATED)
            return Response(status.HTTP_400_BAD_REQUEST)

# Create your views here.
class UserAdvisorList(APIView):
    def get(self,request,format=None):
            user=User.objects.all()
            serializer=UserAdvisorCreateSerializer(user,many=True)
            return Response(serializer.data)

    def post(self,request,format=None):
            print(request.data)
            serializer=UserAdvisorCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status.HTTP_201_CREATED)
            return Response(status.HTTP_400_BAD_REQUEST)

# UserAdvisorCreateSerializer

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
            ExchangeAccount = self.get_object(pk)
            serializer = UserCreateSerializer(ExchangeAccount)
            return Response(serializer.data)




# Create your views here.
class UserLogin(APIView):
    def post(self,request,format=None):
            email=request.data['email']
            password=request.data['password']
            if User.objects.get(email=email,password=password):
                user=User.objects.get(email=email,password=password)
                # print(user.id)
                Token.objects.get_or_create(user=user)
                token = Token.objects.get(user=user)
                res={
                    "auth_token" :token.key,
                    "id":user.id
                }
                return Response(res)
            return Response(status.HTTP_400_BAD_REQUEST)



class CustomUserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
            ExchangeAccount = self.get_object(pk)
            serializer = UserCreateSerializer(ExchangeAccount)
            return Response(serializer.data)



class getReport(APIView): 
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,format=None):
        try:
            # getting report object
            obj = request.user.report
            print("report Found")
            return HttpResponse(obj,content_type='application/pdf')
        except :
            return HttpResponse("Document Is Not Available")


# Create your views here.
class BlogList(APIView):
    def get(self,request,format=None):
        products=Blog.objects.all()
        serializer=BlogSerializer(products,many=True)
        return Response(serializer.data)


class BlogDetail(APIView):
    def get(self, request, pk,format=None):
        blog=Blog.objects.all().filter(id=pk)
        serializer = BlogSerializer(blog,many=True)
        return Response(serializer.data)

# Create your views here.
class FaqList(APIView):
    def get(self,request,format=None):
        products=Faq.objects.all()
        serializer=FaqSerializer(products,many=True)
        return Response(serializer.data)