"""Ecomerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path , include
from EcomerceA.views import ProductListView  ,CollectionsView ,productview ,home , Collections
from django.conf import settings
from django.conf.urls.static import static
from EcomerceA.controller import authview  , cart ,wishlist


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('EcomerceA.urls')),
    # path('',ProductListView.as_view(),name='Home'),
    path('',home,name='home'),
    # 
    path('Collections/',Collections,name='Collections'),
    path('Collections/<str:slug>',CollectionsView,name='CollectionsView'),
    path('Collections/<str:cat_slug>/<str:pro_slug>',productview,name="productview"),
    path('register/',authview.register,name="register"),
    path('login/',authview.loginpage,name="loginpage"),
    path('logout/',authview.logoutpage,name="logout"),

    path('add-to-cart',cart.addtocart,name='addtocart'),
    path('cart',cart.viewcart,name='cart'),
    path('update-cart',cart.updatecart,name="updatecart"),
    path('delete-cart-item',cart.deletecartitem,name="deletecartitem"),


    path('wishlist',wishlist.index,name="wishlist"),
    path('add-to-wishlist',wishlist.addtowishlist,name="addtowishlist"),
    path('delete-wishlist-item',wishlist.deletewishlistitem,name="deletewishlistitem"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)