from django.shortcuts import render,HttpResponse
from  .models import Products
# Create your views here.


def home(request):
    return render(request,'home.html')

def productlist(request):
    all_product=Products.objects.all()
    return render(request,'product.html',{'product':all_product })


def basket(request):
    return render(request,'basket_page.html')

def productitem(request,slug):
    product=Products.objects.get(slug=slug)
    return render(request,'product_item.html',{'product': product})

    
