from django.core.management.base import BaseCommand
from DjTbot.models import TBotGroup


class Command(BaseCommand):
    help = """
    Remove group
    """

    def add_arguments(self, parser):
        parser.add_argument('group_name')

    def handle(self, *args, **options):
        group = TBotGroup.objects.get(name=options['group_name'])
        group.delete()
        print('Deleted {}'.format(group.name))
