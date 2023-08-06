from django.core.management.base import BaseCommand
from DjTbot.models import TBotUser


class Command(BaseCommand):
    help = """
    Delete user
    """

    def add_arguments(self, parser):
        parser.add_argument('user_id')

    def handle(self, *args, **options):
        user = TBotUser.objects.get(id=options['user_id'])
        user.delete()
        print('Deleted {}: {}'.format(user.id, user.name))
