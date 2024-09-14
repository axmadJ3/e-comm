from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
        
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                 verbose_name='Категория', 
                                 related_name='products')
    
    def __str__(self):
        return self.title
