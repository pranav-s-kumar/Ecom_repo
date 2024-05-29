from django.db import models

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name = 'category'   
        verbose_name_plural = 'categories'          #for correcting the plural categories instead of categorys
        
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to="category",blank=True,default='')
    
    def __str__(self):
        return self.name                            #to render category names instead of category 1, category 2 etc
    
class Product(models.Model):
        
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to="category",blank=True,default='')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name                            #to render product names instead of product 1, product 2 etc
