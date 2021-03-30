from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="inventoryhome"),
    path('productcreate', views.createproduct, name="createproduct"),
    path('productlist', views.productlist, name="productlist"),
]