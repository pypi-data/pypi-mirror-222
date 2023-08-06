from django.core.management.base import BaseCommand
from DjTbot.models import TBotUser, TBotGroup


class Command(BaseCommand):
    help = """
    Add User to group
    """

    def add_arguments(self, parser):
        parser.add_argument('group_name')
        parser.add_argument('user_id')

    def handle(self, *args, **options):
        user = TBotUser.objects.get(id=options['user_id'])
        group = TBotGroup.objects.get(name=options['group_name'])
        user.groups.add(group)
