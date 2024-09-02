

from django.db import models

class Book(models.Model):
    GENRES_TYPE=[
        ('Fiction','Fiction'),
        ('Science Fiction','Science Fiction'),
        ('Fantasy','Fantasy'),
        ('Historical','Historical'),
        ('Romance','Romance'),
        ('Mythology','Mythology'),
    ]
    title = models.CharField(max_length=255,verbose_name='Title')
    author = models.CharField(max_length=255,verbose_name='Author')
    published_year = models.IntegerField(max_length=4,null=True,blank=True,verbose_name='Published year')
    description=models.TextField(max_length=1000,null=True,blank=True)
    bookimg=models.ImageField(upload_to='file path',blank=True,null=True,verbose_name='Book image')
    genres = models.CharField(max_length=130, unique=True,choices=GENRES_TYPE)
    pdf= models.FileField(upload_to='file path',blank=True,null=True)

    def __str__(self):
        return self.title
