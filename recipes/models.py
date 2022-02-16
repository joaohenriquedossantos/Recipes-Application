from django.db import models
from datetime import datetime

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    method_of_preparation = models.TextField()
    time_of_preparation = models.IntegerField()
    food_yield = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=datetime.now, blank=True)