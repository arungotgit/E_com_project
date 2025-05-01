"""
URL configuration for E_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .import views
from django.views.generic import RedirectView 


admin.site.site_header = "E-Shop Admin"
admin.site.site_title = "E-Shop Admin Panel"
admin.site.index_title = "Welcome to E-Shop Admin Panel"


urlpatterns = [

    path('admin/', admin.site.urls),
    path('master/', views.Master, name='master'),
    path('', views.Index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),  # Add this line
  
    path('accounts/', include('django.contrib.auth.urls')),
 
    

    #add to cart wale sare links idhar hai
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail/', views.cart_detail, name='cart_detail'),
    
    # contact page url
    path('contact/', views.contact, name='contact'),

    # checkout page url
    path('checkout/', views.Checkout, name='checkout'),

    # order page url
    path('your-order/', views.Your_Order, name='order'),

    # product details page url
    path('product/', views.Product_detail, name='product'),

    # product page url
    path('product/<str:id>', views.Product_page,name='product_page'),

    # this is for product page from index page (main page)
    path('<str:id>', views.Product_page,name='product_page'),

    # search page url
    path('search/', views.Search, name='search'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)