from django.shortcuts import render,HttpResponse

# Create your views here.


def home(request):
    return render(request,'home.html')

def productlist(request):
    return render(request,'product.html')


def basket(request):
    return render(request,'basket_page.html')

def productitem(request,slug):
    # return render(request,'product_item.html')
    
    return HttpResponse(slug)
