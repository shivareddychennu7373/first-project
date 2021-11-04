from django.db import models

# Create your models here.
class Menu(models.Model):
    recipe_name = models.CharField(max_length = 200)
    recipe_ingre = models.CharField(max_length = 200)
    recipe_process = models.TextField()

    def __str__(self):
        return self.recipe_name