from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from materials.models import Subscription


@shared_task
def mail_update_course_info(course_id):
    """Отправка сообщения об обновлении курса"""
    subscription_course = Subscription.objects.select_related('course', 'user').filter(course_id=course_id)
    print(f"Найдено {len(subscription_course)} подписок на курс {course_id}")
    for subscription in subscription_course:
        print(f"Отправка электронного письма на {subscription.user.email}")
        send_mail(
            subject="Обновление материалов курса",
            message=f'Курс {subscription.course.title} был обновлен.',
            from_email=EMAIL_HOST_USER,
            recipient_list=[subscription.user.email],
            fail_silently=False
        )
