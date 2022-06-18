
from django.db import models
from django.contrib.auth.models import AbstractUser
from .Role import Role
# Create your models here.


class Account(AbstractUser):
    username = models.CharField(unique=True, max_length=29)
    password = models.TextField(max_length=5000)
    role = models.ForeignKey(
        Role, blank=True, null=True, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'Account'

    def __str__(self) -> str:
        return f"{self.username}"
