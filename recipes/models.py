from django.db import models

# Create your models here.

class RecipeChoices(models.TextChoices):
    DESSERTS = "desserts" , "D"
    ENTREES = "entrees" , "E"
    APPETIZERS = "appetizers" , "A"

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    detail =models.TextField()
    date_created =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=10,choices=RecipeChoices.choices,default=RecipeChoices.APPETIZERS)
    image = models.ImageField(upload_to="images/",default="default.jpg")

    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ['-date_created']


