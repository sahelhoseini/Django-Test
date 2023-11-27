from django.shortcuts import render,HttpResponse
from  .models import Products,Imageofslider
# Create your views here.


def home(request):
    slider=Imageofslider.objects.all().order_by('-created')
    slider=slider[:4]
    product=Products.objects.all().order_by('-created')
    product=product[:4]
    return render(request,'home.html',{'product':product ,'slider':slider})

def productlist(request):
    all_product=Products.objects.all().order_by('-created')
    return render(request,'product.html',{'product':all_product })


def basket(request):
    return render(request,'basket_page.html')

def productitem(request,slug):
    product=Products.objects.get(slug=slug)
    return render(request,'product_item.html',{'product': product})

    
