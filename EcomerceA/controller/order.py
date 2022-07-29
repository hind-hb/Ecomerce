from django.contrib import messages
from django.shortcuts import render , redirect

from EcomerceA.models import  Order , OrderItem
from django.contrib.auth.decorators import login_required


def index(request):
    orders=Order.objects.filter(user=request.user)
    context={'orders':orders}
    return render(request,'store/order/order.html',context)


def view(requset,tracking_no):
    order=Order.objects.filter(tracking_no=tracking_no)
    ordersitems = OrderItem.objects.filter(order=order)
    context={'order':order,'ordersitems':ordersitems}
    return render(requset   ,'store/order/view.html',context)



