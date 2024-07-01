from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.

def shop(request):
    if request.method=="POST":
        print("Entered")
        search = request.POST.get('search')
        if search:
            products = Products.objects.filter(name__icontains=search)
            print(search)
        else:
            products = Products.objects.all()
    else:
        products = Products.objects.all()
    category = Category.objects.all()
    tags = Tags.objects.all()
    return render(request,"shop.html",{'p':products, 'c':category, 't':tags})


def shop_category(request,category):
    products = Products.objects.filter(cate = category)
    category = Category.objects.all()
    tags = Tags.objects.all()
    return render(request,"shop.html",{'p':products, 'c':category, 't':tags})


def shop_tag(request,tag):
    products = Products.objects.filter(tags = tag)
    category = Category.objects.all()
    tags = Tags.objects.all()
    return render(request,"shop.html",{'p':products, 'c':category, 't':tags})


def single_product(request,pk):
    if request.method == "POST":
        product = Products.objects.get(id=pk)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        a = ProductRequest(product_name = product, name = name, email = email, phone= phone, msg = msg)
        a.save()
        messages.success(request, "Form submitted successsfully")
    product = Products.objects.filter(id=pk)
    return render(request,"single-product.html",{'p':product})