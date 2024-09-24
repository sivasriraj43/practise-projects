from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=250,db_index=True)
    slug =models.SlugField(max_length=250,unique=True)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list-category',args=[self.slug])
    
class Product(models.Model):
    title=models.CharField(max_length=250)
    brand=models.CharField(max_length=250,default='unbranded')
    description=models.TextField(blank=True)
    slug=models.SlugField(max_length=250)
    price=models.DecimalField(max_digits=4,decimal_places=2)
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE,null=True)
    class Meta:
        verbose_name="Product"
        verbose_name_plural='Products'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product-info',args=[self.slug])


