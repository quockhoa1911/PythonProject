from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=50, default="USER")

    class Meta:
        db_table = "Role"

    def __str__(self) -> str:
        return f"{self.name}({self.id})"
