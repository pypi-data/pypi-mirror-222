from django.core.management.base import BaseCommand
from DjTbot.models import TBotGroup


class Command(BaseCommand):
    help = """
    List groups
    """

    def handle(self, *args, **options):
        groups = TBotGroup.objects.all()
        for group in groups:
            print('{}: {}'.format(group.id, group.name))
