from django.db import models

# Create your models here.
class Product(models.Model):
    # sku = models.CharField(max_length=29,primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateField(auto_now=True)

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
    payment_status = models.CharField(
        max_length=1,choices=PAYMENT_STATUS_CHOICES,default='P'
    )


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=299)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)


class C