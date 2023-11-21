from django.shortcuts import render,HttpResponse

# Create your views here.


def productlist(request):
    return render(request,'product.html')
    


def home(request):
    return render(request,'home.html')