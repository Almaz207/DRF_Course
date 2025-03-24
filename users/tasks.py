from celery import shared_task
from datetime import timedelta
from django.utils import timezone

from users.models import CustomUser


@shared_task
def check_last_login():
    """Проверка последнего входа пользователей и отключение неактивных пользователей"""
    users = CustomUser.objects.filter(last_login__isnull=False)
    today = timezone.now()
    for user in users:
        if today - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
            print(f'Пользователь {user.email} отключен')
        else:
            print(f'Пользователь {user.email} активен')
