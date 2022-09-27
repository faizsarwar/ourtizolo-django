from django.urls import include, path
from .views import * 

urlpatterns = [
path('CustomUser/',UserList.as_view(),name='CustomUserList'),
path('CustomUser/login',UserLogin.as_view(),name='CustomUserLogin'),
path('CustomUser/document',getReport.as_view(),name='CustomUserDocument'),
path('CustomUser/<int:pk>/',UserDetail.as_view(),name='CustomUserDetail'),
]
