from django.core.management.base import BaseCommand
from DjTbot.models import TBotGroup


class Command(BaseCommand):
    help = """
    Add A group
    """

    def add_arguments(self, parser):
        parser.add_argument('group_name')

    def handle(self, *args, **options):
        TBotGroup.objects.create(name=options['group_name'])
