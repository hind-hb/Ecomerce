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
    trending=models.BooleanField(default=False,help_text="0 = default, 1 = Hidden")
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
    trending=models.BooleanField(default=False,help_text="0 = default, 1 = Hidden")
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

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=150,null=False)
    lname=models.CharField(max_length=150,null=False)    
    email=models.CharField(max_length=150,null=False)
    phone=models.CharField(max_length=150,null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=150,null=False)
    state=models.CharField(max_length=150,null=False)
    country=models.CharField(max_length=150,null=False)
    pincode=models.CharField(max_length=150,null=False)
    total_price=models.FloatField(null=False)
    payment_mode=models.CharField(max_length=150,null=False)
    payment_id=models.CharField(max_length=250,null=True)
    orderstatuses=(
    ('Pending','Pending'),
    ('Out For Shipping' ,'Out For Shipping '),
    ('Completed','Completed'),


    )
    status=models.CharField(max_length=150,choices=orderstatuses,default='Pending')
    message=models.TextField(null=True)
    tracking_no=models.CharField(max_length=150,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id,self.tracking_no)

class OrderItem(models.Model):
        order=models.ForeignKey(Order,on_delete=models.CASCADE)
        product=models.ForeignKey(Product,on_delete=models.CASCADE)    
        price=models.FloatField(null=False)
        quantity=models.IntegerField(null=False)
        
        def __str__(self) :
            return '{} {}' .format(self.order.id,self.order.tracking_no)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name= models.CharField(max_length=150,null=False, default='')
    last_name= models.CharField(max_length=150,null=False, default='')
    profile_image = models.ImageField(upload_to=get_file_path, null=True,blank=True)
    phone=models.CharField(max_length=150,null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=150,null=False)
    state=models.CharField(max_length=150,null=False)
    country=models.CharField(max_length=150,null=False)
    pincode=models.CharField(max_length=150,null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username