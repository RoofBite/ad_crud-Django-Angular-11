from django.db import models
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.TextField()
    ordering = models.IntegerField()

    def __str__(self):
        return self.name

class Offer(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0.0),])
    created_at  = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)