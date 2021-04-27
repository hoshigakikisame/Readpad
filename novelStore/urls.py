"""novelStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('search/', views.search, name="search"),
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('userAuth/', include(('userAuth.urls', 'userAuth'), namespace="userAuth")),
    path('novel/', include(('novel.urls', 'novel'), namespace="novel")),
    path('staff/', views.staffPage, name="staffPage"),
    path('konfirmasi/<str:id_pesanan>', views.konfirmasi, name="konfirmasi"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)