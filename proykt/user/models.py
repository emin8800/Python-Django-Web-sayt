from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='users/', blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        # 'auth.User.groups' çakışmasını çözmek için
        # related_name parametresini kullanıyoruz
        app_label = 'user'
        abstract = False
        swappable = 'AUTH_USER_MODEL'
        verbose_name = "User"
        verbose_name_plural = "Users"
