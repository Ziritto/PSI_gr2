from django.db import models

# Create your models here.

class alcoholCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class alcohol(models.Model):
    name = models.CharField(max_length=45)
    alcohol_category = models.ForeignKey(alcoholCategory, on_delete=models.CASCADE)
    taste = models.CharField(max_length=45)
    how_strong = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Client(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    gender = models.CharField(max_length=2)
    address = models.CharField(max_length=100)

class Order(models.Model):
    client = models.ForeignKey(Client,  on_delete=models.CASCADE)
    alcohol = models.ForeignKey(alcohol,  on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
