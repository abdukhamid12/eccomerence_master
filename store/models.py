from django.db import models

# Create your models here.


# становится базовым моделем и берется ворс от этого модели
class Time(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # класс мета обеспечивает чтобы модель не создовался в базе
    class Meta:
        abstract = True

class Category(Time):
    name = models.CharField(max_length=100)
    decscription = models.TextField()

    def __str__(self):
        return self.name

class Product(Time):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    decscription = models.TextField()
    image = models.ImageField(upload_to='store_product/')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name