from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Flower(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='flowers')
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='flowers/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name