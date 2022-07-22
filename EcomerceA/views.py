
from django.shortcuts import render , redirect
from EcomerceA.api.serializers import CatgeorySerializer , ProductSerializer
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from EcomerceA.models import Category , Product
from rest_framework import generics
from django.contrib import messages


# Create your views here.
class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatgeorySerializer

class DetailCatgory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CatgeorySerializer

class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    fields = ['__all__']

# def Collections(request):
#     category = Category.objects.all()
#     context = {'category':category}
#     return render (request , "Collections.html",context)
#     # template_name = 'Collections.html'
#     # fields = ['__all__']

def CollectionsView(request , slug):
    if (Category.objects.filter(slug=slug)):
        products = Product.objects.filter(slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products' : products,'category':category}
        return render (request , "store/products.html",context)
    else :
        messages.warning(request,"No such category found")
        return redirect("store/Collections.html")

def productview(request,cat_slug,pro_slug):
    if (Category.objects.filter(slug = cat_slug)):
        if (Product.objects.filter(slug = pro_slug)):
            products = Product.objects.filter(slug = pro_slug).first()
            context = {'products':products}
        
        else:
            messages.warning(request,"No such product found")
            return redirect("store/Collections.html")
    else:
            messages.warning(request,"No such category found")
            return redirect("store/Collections.html")
    return render(request,'store/view.html',context)

def home(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request,'store/index.html',context)
    
def Collections(request):
    category = Category.objects.all()
    context = {'category':category}
    return render(request,'store/Collections.html',context)


