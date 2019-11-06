import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from geoposition.fields import GeopositionField


class Realuser(AbstractUser):
    # address = models.CharField(max_length=100)
    token = models.CharField(max_length=255, default="111", null=True)

    class Meta:
        db_table = "realuser"
        verbose_name_plural = "User"


class Category(models.Model):
   category_name = models.CharField(max_length=50, null=True)

   class Meta:
       db_table = "category"
       verbose_name_plural = "Category"

   def __str__(self):
       return self.category_name


class Type(models.Model):
    type_name = models. CharField(max_length=50)

    class Meta:
       db_table = "type"
       verbose_name = "Type"

    def __str__(self):
        return self.type_name


class Ingredients(models.Model):
    ingredients = models.CharField(max_length=100)

    class Meta:
       db_table = "ingredients"
       verbose_name_plural = "Ingredients"

    def __str__(self):
       return self.ingredients


class Recipe(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    ingredients = models.ManyToManyField(Ingredients, blank=True)
    type_name = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type')
    recipe = models.CharField(max_length=100, null=True, blank=True)
    prep = models.CharField(max_length=100, null=True, blank=True)
    cook = models.CharField(max_length=100, null=True, blank=True)
    yields = models.CharField(max_length=100, null=True, blank=True)
    img = models. FileField(blank=True, null=True)
    steps = RichTextField(blank=True, null=True)
    date = models.DateField(default=datetime.date.today, null=True, blank=True)

    class Meta:
       db_table = "recipe"
       verbose_name = "Recipe"

    def __str__(self):
        return self.recipe


class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipes',null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=True, null=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    rate = models.IntegerField(blank=True,null=True)
    # date = models.DateTimeField(auto_now_add=True, blank=True, default =0)


    class Meta:
        db_table = "review"
        verbose_name = "Review"

    def __str__(self):
        return self.name


class Slider(models.Model):
    slider_image = models.FileField(blank=True, null=True)
    slider_caption1 = models.CharField(max_length=100, null=True, blank=True)
    slider_caption2 = models.CharField(max_length=100, null=True, blank=True)
    slider_caption3 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "slider"
        verbose_name_plural  = "Slider"

    def __str__(self):
        return self.slider_image.url

class Links(models.Model):
    icon_name = models.CharField(max_length=100, blank=True, null=True)
    social_url = models.URLField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "links"
        verbose_name_plural = "Social link"

    def __str__(self):
        return self.icon_name

class Contact(models.Model):
    contact_name = models.CharField(max_length=100,blank=True, null=True)
    contact_email = models.EmailField(max_length=70, blank=True, null=True)
    contact_subject = models.CharField(max_length=100,blank=True, null=True)
    contact_message = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "contact"
        verbose_name_plural = "contact"

    def __str__(self):
        return self.contact_name

class ImageSlider(models.Model):
    image = models. FileField(blank=True, null=True)

    class Meta:
        db_table = "imageslider"
        verbose_name_plural = "Image Slider"

    def __str__(self):
        return self.image.url

class About(models.Model):
    about_caption = models.CharField(max_length=100,blank=True,null=True)
    about_content = models.CharField(max_length=255,blank=True,null=True)
    about_image = models.FileField(blank=True, null=True)
    about_text = models.CharField(max_length =100,blank=True,null=True)

    class Meta:
        db_table = "about"
        verbose_name_plural="About"

    def __str__(self):
        return  self.about_caption

class AboutChild(models.Model):
    about_icons = models.FileField(blank=True, null=True)
    about_number = models.CharField(max_length=100,blank=True, null=True)
    about_iconitem = models.CharField(max_length=100,blank=True, null=True)

    class Meta:
        db_table = "aboutchild"
        verbose_name_plural = "About Child"

    def __str__(self):
        return self.about_iconitem



class GoogleMap(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        db_table = "googlemap"
        verbose_name_plural = "Google Map"

    def __str__(self):
        return self.name

class Rating(models.Model):
    recipe_name = models.CharField(max_length=100, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    average = models.IntegerField(null=True, blank=True)
    image = models.FileField(blank=True, null=True)
    # date = models.DateTimeField(auto_now_add=True, blank=True, default =0)

    class Meta:
        db_table = "rating"
        verbose_name_plural = "Rating"

    def __str__(self):
        return self.recipe_name