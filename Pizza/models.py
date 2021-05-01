from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to="images", blank=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name
