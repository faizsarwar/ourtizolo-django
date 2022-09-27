from django.urls import path, include
from .views import *

urlpatterns = [
    path('Testemonials/',TestemonialList.as_view()),
    path('Research/',ResearchList.as_view()),
    path('Research/<int:pk>/', ResearchDetail.as_view()),
    path('Blogs/',BlogList.as_view()),
    path('Blogs/<int:pk>/', BlogDetail.as_view()),
    path('Press/',PressList.as_view()),
    path('Press/<int:pk>/',PressDetail.as_view()),
    path('Faqs/',FaqList.as_view())
]