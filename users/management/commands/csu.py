from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CustomUser.objects.create(email="admini@mail.ru")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("12345678")
        user.save()
