from django.contrib import messages
from django.shortcuts import render , redirect
from django.http.response import JsonResponse
from EcomerceA.models import Product , Cart
from django.contrib.auth.decorators import login_required

def index (request):
    rawcart=Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.stock:
            Cart.objects.delete(id=item.id)
    cartitem  = Cart.objects.filter(user=request.user)
    total_price=0
    for item in cartitem:
        total_price=total_price +item.product.price * item.product_qty

    context={'cartitem':cartitem,'total_price':total_price}
    return render(request,'store/checkout.html',context)