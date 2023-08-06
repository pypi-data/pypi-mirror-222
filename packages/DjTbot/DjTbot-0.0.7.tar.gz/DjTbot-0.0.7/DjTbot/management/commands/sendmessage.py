from django.core.management.base import BaseCommand
import logging
from DjTbot.utils import send_message, get_group_members, get_user_id, get_all_ids


logger = logging.getLogger("dj_tbot")


class Command(BaseCommand):
    help = """
    Send message
    """

    def handle(self, *args, **options):

        if options.get('user_id'):
            self.try_send_message(options['user_id'], options['message'], options['http_proxy'])
        elif options.get('user'):
            self.try_send_message(get_user_id(options['user']), options['message'], options['http_proxy'])
        elif options.get('group'):
            for user_id in get_group_members(options['group']):
                self.try_send_message(user_id, options['message'], options['http_proxy'])

        elif options.get('all'):
            for user_id in get_all_ids():
                self.try_send_message(user_id, options['message'], options['http_proxy'])

    @staticmethod
    def try_send_message(user_id, message, http_proxy):
        try:
            send_message(user_id, message, http_proxy)
        except Exception as e:
            print(f"Exception sending message to {user_id}: {str(e)}")

    def add_arguments(self, parser):
        recipient = parser.add_mutually_exclusive_group(required=True)
        recipient.add_argument('--user', help='User Name')
        recipient.add_argument('--user-id', help='User telegram id')
        recipient.add_argument('--group', help='Group Broadcast')
        recipient.add_argument('--all', help='All users', action='store_true')
        parser.add_argument('message', help='Message to send')
        parser.add_argument('--http-proxy',
                            help='Proxy URL. Examples: http://USERNAME:PASSWORD@PROXY_HOST:PROXY_PORT/')
