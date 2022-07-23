from itertools import product
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime
import os

def get_file_path(request,filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/',filename)


# Create your models here.
class Category (models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to=get_file_path , null=True , blank = True)
    # status = models.BooleanField(default=False,help_text="0-default,1=Hidden")
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return  self.title 

class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='Food')
    slug=models.CharField(max_length=150,null=False,blank=False)
    # status = models.BooleanField(default=False,help_text="0-default,1=Hidden")
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    # img = models.ImageField(upload_to=get_file_path,height_field=None,width_field=None,max_length=None)
    img = models.ImageField(upload_to=get_file_path , null=True , blank = True)
    sellerInfo = models.CharField(max_length=255)
    Date = models.DateField(auto_now_add=True)

    class Meta :
        ordering = ['-Date']
    def __str__(self):
        return self.title
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)