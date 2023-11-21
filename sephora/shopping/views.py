from django.shortcuts import render,HttpResponse

# Create your views here.


def productlist(request):
    pass


def home(request):
    return render(request,'home.html')