from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True, verbose_name="email"
    )  # нужно добавить help_text
    phone_number = models.CharField(
        max_length=25, null=True, blank=True, verbose_name="номер телефона"
    )
    city = models.CharField(max_length=75, null=True, blank=True, verbose_name="Город")
    avatar = models.ImageField(
        null=True, blank=True, upload_to="users/avatar", verbose_name="аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
