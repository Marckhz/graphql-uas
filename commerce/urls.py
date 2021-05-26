from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HelloWorld, say_hello, ShopViewSet

router = DefaultRouter()
router.register(r'shop',ShopViewSet, basename='shop')

urlpatterns =[
    path('', include(router.urls)),
    path('home', say_hello, name='home'),
    path("home2", HelloWorld.as_view(), name='home2')
]