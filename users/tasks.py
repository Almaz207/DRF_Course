from celery import shared_task

from dateutil.relativedelta import relativedelta
from django.utils import timezone

from users.models import CustomUser


@shared_task
def check_last_login():
    """Проверка последнего входа пользователей и отключение неактивных пользователей"""
    month_ago = timezone.now() - relativedelta(months=1)
    users_to_block = CustomUser.objects.filter(is_active=True, last_login__lte=month_ago)
    users_to_block.update(is_active=False)
