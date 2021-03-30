from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.product_name


    
