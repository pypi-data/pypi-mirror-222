from django.core.management.base import BaseCommand
from DjTbot.models import TBotUser


class Command(BaseCommand):
    help = """
    List Users
    """

    def handle(self, *args, **options):
        users = TBotUser.objects.all()
        for user in users:
            print('{}: {}'.format(user.id, user.name))
