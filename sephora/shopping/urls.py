from django.urls import path
from . import views


urlpatterns=[
    path('productlist/', views.productlist , name='productlist'),
    path('<slug>', views.productitem , name='productitem'),
    path('basket/', views.basket , name='basketpage'),
    path('', views.home , name='home'),
]

