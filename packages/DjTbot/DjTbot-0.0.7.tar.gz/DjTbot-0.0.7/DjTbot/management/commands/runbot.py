from django.core.management.base import BaseCommand
import logging
from django.conf import settings
from DjTbot.core.telegram_lib import Bot
from DjTbot.core.errors import ConfigurationError
from DjTbot.utils import setting_or_env

logger = logging.getLogger("DjTbot")


class Command(BaseCommand):
    help = """
    Run your bot, there can only be one running command
    """

    def add_arguments(self, parser):
        parser.add_argument('--http-proxy', help='Proxy URL. Examples: http://USERNAME:PASSWORD@PROXY_HOST:PROXY_PORT/ | ')

    def handle(self, *args, **options):
        logger.info(f'Starting Telegram bot. {self.version}')
        if options['http_proxy']:
            Bot(self.api_key, http_proxy=options['http_proxy'])
        else:
            Bot(self.api_key)

    @property
    def version(self):
        return setting_or_env('VERSION', '0.0.0')

    @property
    def api_key(self):
        api_key = setting_or_env('TELEGRAM_API_KEY', None)
        if api_key is None:
            raise ConfigurationError('TELEGRAM_API_KEY is not set, '
                                     'please set it in your settings.py or as an environment variable')
        return api_key
