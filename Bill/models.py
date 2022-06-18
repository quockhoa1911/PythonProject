from re import T
from django.db import models
from Fruitapp.models import Fruits

# Create your models here.


class Bill(models.Model):
    status = models.BooleanField(default=1)
    totalPrice = models.IntegerField(default=0)
    code = models.IntegerField()
    createAt = models.DateTimeField(auto_now_add=True)
    ListFruits = models.ManyToManyField(Fruits, through='DetailBill')

    class Meta:
        db_table = "Bill"


class DetailBill(models.Model):
    bill = models.ForeignKey(
        Bill, on_delete=models.CASCADE, blank=True, null=True)
    fruit = models.ForeignKey(
        Fruits, on_delete=models.CASCADE, blank=True, null=True)
    weight = models.FloatField()

    class Meta:
        db_table = "Detailbill"
