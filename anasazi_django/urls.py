"""anasazi_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header='Anasazi Admin Portal'
admin.site.site_title='Welcome Anasazi admin panel'
admin.site.index_title='Welcome Anasazi admin panel'

urlpatterns = [
    path('jet/',include('jet.urls')),
    path('jet/dashboard',include('jet.dashboard.urls','jet-dashboard')),
    path('admin/', admin.site.urls),
    path('api/v1/',include('djoser.urls')),
    path('api/v1/',include('djoser.urls.authtoken')),
    path('api/v1/',include('products.urls')),
    path('api/v1/',include('extras.urls')),
    path('api/v1/',include('order.urls')),
    path('api/v1/',include('userapp.urls')),
    path('api/v1/',include('gtl.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)