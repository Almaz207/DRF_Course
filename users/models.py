from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Course, Lesson


class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True, verbose_name="email", help_text="email пользователя"
    )

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


class Payment(models.Model):
    CASH = "cash"
    NON_CASH = "non_cash"
    PAYMENT_OPTIONS = ((CASH, "Наличный"), (NON_CASH, "Безналичный"))
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="payments",
    )
    time = models.DateTimeField(
        verbose_name="Дата оплаты",
        help_text="Введите дату",

        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Оплаченный курс",
        related_name='payments'
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный урок",
        null=True,
        blank=True,
        related_name='payments'
    )
    price = models.PositiveIntegerField(default=0, verbose_name="Стоимость покупки")
    method = models.CharField(
        max_length=20,
        choices=PAYMENT_OPTIONS,
        default=CASH,
        verbose_name="Способ оплаты",
    )
    link = models.URLField(
        max_length=400,
        verbose_name="Ссылка на оплату",
        help_text="Укажите ссылку на оплату",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return self.payment_method
