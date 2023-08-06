from django.core.management.base import BaseCommand
from DjTbot.utils import get_group, create_user


class Command(BaseCommand):
    help = """
    Creates the bot Admin Users and group if it does not exist
    """

    def handle(self, *args, **options):
        admin_group = get_group('Admins')
        telegram_id = input('User telegram ID? ')
        name = input('User full name?')
        user = create_user(telegram_id, name)
        user.groups.add(admin_group)
