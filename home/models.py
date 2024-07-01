from django.db import models

# Create your models here.

class HomeImages(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100, null=True, blank=True)
    
    def save(self,*args, **kwargs):
        if self.image:
            self.title = self.image.name
        
        super().save(*args, **kwargs)
   
    def __str__(self):
        return self.image.name
    

class About(models.Model):
    heading = models.CharField(max_length=225)
    body = models.CharField(max_length=525)


class review(models.Model):
    body = models.CharField(max_length=225)
    name = models.CharField(max_length=100)


class faq(models.Model):
    heading = models.CharField(max_length=225)
    body = models.CharField(max_length=225)
    number = models.CharField(max_length=225, null = True)


class ContactForm(models.Model):
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    subject = models.CharField(max_length=225)
    message = models.CharField(max_length=225)

    def __str__(self):
        return self.name


