from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='serious@yandex.ru',
            first_name='Alexander',
            last_name='Rychagov',
            is_superuser=True,
            is_staff=True,
            is_active=True,
            verified=True
        )
        user.set_password('CRTSz7v4')
        user.save()
