from django.db import models

# Create your models here.


class Fruits(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    season = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField()
    uint = models.CharField(default='KG', max_length=50)
    currencyunit = models.CharField(max_length=50, default="VND")
    remain = models.IntegerField()
    sold = models.FloatField()
    avatar = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Fruits"

    def __str__(self) -> str:
        return f"{self.name}({self.id})"
