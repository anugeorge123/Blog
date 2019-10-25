import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


import os
#
# def get_image_path(instance, filename):
#     return os.path.join('photos', str(instance.id), filename)

class Realuser(AbstractUser):
    address = models.CharField(max_length=100)


    class Meta:
        db_table = "realuser"


class Category(models.Model):
   category_name = models.CharField(max_length=50, null=True)


   class Meta:
       db_table = "category"


class Type(models.Model):
    type_name = models. CharField(max_length=50)

    class Meta:
       db_table = "type"


class Ingredients(models.Model):
    ingredients = models.CharField(max_length=100)


    class Meta:
       db_table = "ingredients"


class Recipe(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE, related_name='ingredient')
    type_name = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type')
    recipe = models.CharField(max_length=100, null=True, blank=True)
    prep = models.CharField(max_length=100, null=True, blank=True)
    cook = models.CharField(max_length=100, null=True, blank=True)
    yields = models.CharField(max_length=100, null=True, blank=True)
    # img = models. ImageField(upload_to=get_image_path, blank=True, null=True)
    # steps = models.RichTextField()
    date = models.DateField(default=datetime.date.today, null=True, blank=True)


class Meta:
       db_table = "recipe"


class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipes')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        db_table = "review"
