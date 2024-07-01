from django.shortcuts import render
from .models import *
from products.models import Products
from django.contrib import messages

# Create your views here.

def index(request):
    about = About.objects.all()
    r = review.objects.all()
    f = faq.objects.all()
    products = Products.objects.all()
    context = {'a':about,'r':r,'f':f,'p':products}
    return render(request,"index.html",context)


def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        subject = request.POST.get('subject')
        message = request.POST.get('msg')
        a = ContactForm(name = name, email = email, phone=phone, subject = subject, message = message)
        a.save()
        messages.success(request, "Form Submitted successfully")
    return render(request,"contact.html")
