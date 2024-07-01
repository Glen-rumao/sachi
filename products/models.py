from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name
    
    
class Products(models.Model):
    name = models.CharField(max_length=225)
    price = models.IntegerField()
    desc = models.TextField(null = True, blank=True)
    detailed_desc = models.TextField(null = True, blank=True)
    ad_desc = models.TextField(null = True, blank=True)
    cate = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, blank=True)
    tags = models.ForeignKey(Tags, null=True, on_delete=models.CASCADE, blank=True)
    banner = models.ImageField(upload_to='products/', null=True, blank=True)
    image1 = models.ImageField(upload_to='products/')
    small_image = models.ImageField(upload_to='products/', null=True, blank=True)
    small_image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    small_image3 = models.ImageField(upload_to='products/',null=True, blank=True)
    large_image = models.ImageField(upload_to='products/',null=True, blank=True)
    large_image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    large_image3 = models.ImageField(upload_to='products/',null=True, blank=True)

    def __str__(self):
        return self.name
    

class ProductRequest(models.Model):
    product_name = models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=225,null=True)
    email = models.CharField(max_length=225,null=True)
    phone = models.CharField(max_length=225,null=True)
    msg = models.CharField(max_length=225,null=True)

    def __str__(self):
        return self.product_name.name
