from django.core.management.base import BaseCommand
from DjTbot.utils import create_user


class Command(BaseCommand):
    help = """
    Add User
    """

    def handle(self, *args, **options):
        create_user(options['id'], options['name'])

    def add_arguments(self, parser):
        parser.add_argument('id', help='Telegram user id')
        parser.add_argument('name', help='User name')