from django.urls import path
from .views import (
    Home,
    ProductDetails,
    CategoryDetails,
    ProductList,
    SearchProducts,
    Profile
)
from .views import contact_view

urlpatterns = [
    path('',Home.as_view(),name='home'),
    #path('',About.as_view(),name='about'),
    path('product-details/<str:slug>/',ProductDetails.as_view(),name='product-details'),
    path('contact/', contact_view, name='contact'),
    path('category-details/<str:slug>/',CategoryDetails.as_view(),name='category-details'),
    path('product-list/',ProductList.as_view(),name='product-list'),
    #path('contact/', ContactView.as_view(), name='contact'),
    path('profile/',Profile.as_view(),name='profile'),
    path('search-products/',SearchProducts.as_view(),name='search-products'),
]
