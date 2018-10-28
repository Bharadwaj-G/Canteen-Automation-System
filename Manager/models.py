from django.db import models


# Create your models here.

class Food_items(models.Model):
    Food_id = models.IntegerField(null=False, unique=True, primary_key=True)
    Food_Name = models.CharField(max_length=225)
    Food_Price = models.IntegerField()


class Quantity(models.Model):
    Food_id = models.ForeignKey(Food_items, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)


class Tables(models.Model):
    Table_id = models.IntegerField(null=False, unique=True, primary_key=True)
    status = models.BooleanField(default=True)


class Available_Towns(models.Model):
    Towns = models.CharField(max_length=225, unique=True)
