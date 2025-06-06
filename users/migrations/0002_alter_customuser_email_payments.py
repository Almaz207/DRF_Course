# Generated by Django 5.1.5 on 2025-03-11 20:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0005_alter_lesson_course"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                help_text="email пользователя",
                max_length=254,
                unique=True,
                verbose_name="email",
            ),
        ),
        migrations.CreateModel(
            name="Payments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_time",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Введите дату",
                        null=True,
                        verbose_name="Дата оплаты",
                    ),
                ),
                (
                    "price",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Стоимость покупки"
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("cash", "Наличный"), ("non_cash", "Безналичный")],
                        default="cash",
                        max_length=20,
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "link",
                    models.URLField(
                        blank=True,
                        help_text="Укажите ссылку на оплату",
                        max_length=400,
                        null=True,
                        verbose_name="Ссылка на оплату",
                    ),
                ),
                (
                    "payment_course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                        verbose_name="Оплаченный курс",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Оплата",
                "verbose_name_plural": "Оплаты",
            },
        ),
    ]
