from django.db import models

# Create your models here.

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')




class Product(models.Model):
    # sku = models.CharField(max_length=29,primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    MEMBERSHIP_CHOICES = [
        ('B','Bronze'),
        ('S','Silver'),
        ('G','Gold'),
    ]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=300,unique=True)
    phone = models.IntegerField(max_length=10)
    birh_date = models.DateField(null=True,blank=True)
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default='B')

class Order(models.Model):
    PAYMENT_STATUS_CHOICES =[
        ('P','Pending'),
        ('C','Complete'),
        ('F','Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default='P')
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity= models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=299)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

