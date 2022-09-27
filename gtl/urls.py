from django.urls import include, path
from .views import * 

urlpatterns = [
path('GtlForm/',GtlFormList.as_view(),name='GtlForm'),
]
