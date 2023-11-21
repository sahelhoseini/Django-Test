from django.shortcuts import render,HttpResponse

# Create your views here.


def home(request):
    return render(request,'home.html')

def productlist(request):
    return render(request,'product.html')
    
def productitem(request):
    return render(request,'product_item.html')
