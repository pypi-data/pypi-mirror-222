import os
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = """
    Create / Remove secret settings file
    """

    def handle(self, *args, **options):
        remove_config = input('Would you like to remove the current secret file? [Y/n]')
        if remove_config.lower() == 'y':
            os.remove(settings.SECRET_PATH)
            print('Run: python manage.py setup again to generate a new config file')
