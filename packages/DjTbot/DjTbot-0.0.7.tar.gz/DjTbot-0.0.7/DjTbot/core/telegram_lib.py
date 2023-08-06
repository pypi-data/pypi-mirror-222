# -*- coding: utf-8 -*-
import os
import logging
import traceback
from importlib import import_module
from .network import wait_for_internet
from .commands import Command, HELP
from .listeners import Listener
from telegram.ext import Updater, CommandHandler, MessageHandler
from django.conf import settings
from DjTbot.utils import get_group_members

logger = logging.getLogger("DjTbot")


def load_app_commands(app):
    try:
        import_module(app + '.commands')
        logger.info(f'Loaded telegram commands from {app}')
    except ModuleNotFoundError:
        logger.debug(f'No commands found in {app}')


def load_app_listeners(app):
    try:
        import_module(app + '.listeners')
        logger.info(f'Loaded telegram listeners from {app}')
    except ModuleNotFoundError:
        logger.debug(f'No commands found in {app}')


def load_app_handlers():
    for app in settings.INSTALLED_APPS:
        load_app_commands(app)
        load_app_listeners(app)


load_app_handlers()


class Bot(object):
    def __init__(self, api_key, http_proxy=None, daemon=True):
        if http_proxy:
            self.updater = Updater(token=api_key, request_kwargs=self.proxy(http_proxy), use_context=True)
        else:
            self.updater = Updater(token=api_key, use_context=True)
        self.bot = self.updater.bot
        self.dispatcher = self.updater.dispatcher
        self.dispatcher.add_error_handler(self.error_handler)
        self.load_handlers()
        self.load_listeners()
        wait_for_internet(http_proxy=http_proxy)

        if daemon:
            self.updater.start_polling()
            self.updater.idle()

    def proxy(self, http_proxy=None):
        os.environ['http_proxy'] = http_proxy
        os.environ['https_proxy'] = http_proxy
        return {
            'proxy_url': http_proxy
        }

    def load_handlers(self):
        commands = Command.__subclasses__()
        for command in commands:
            command = command()
            if isinstance(command.command, list):
                for cmd in command.command:
                    self.add_command_handler(cmd, command.__call__)
            else:
                self.add_command_handler(command.command, command.__call__)
            self.add_help(command)

    def add_command_handler(self, cmd, func):
        handler = CommandHandler(cmd, func)
        self.dispatcher.add_handler(handler)

    @staticmethod
    def add_help(command):
        if isinstance(command.command, list):
            HELP[", ".join(['/' + cmd for cmd in command.command])] = \
                {'help': command.help_text, 'groups': command.allowed_groups}
        else:
            HELP.setdefault(command.help_text, []).append('/' + command.command)

    def load_listeners(self):
        listeners = Listener.__subclasses__()
        for listener in listeners:
            lsner = listener()
            self.add_message_handler(lsner.filters, callback=lsner.__call__)

    def add_message_handler(self, filters, callback):
        handler = MessageHandler(filters, callback)
        self.dispatcher.add_handler(handler)

    def error_handler(self, update, context):
        """Log Errors caused by Updates."""
        message = f"Update caused error\n" \
                  f"Message from: {update['message']['chat']['username']}\n" \
                  f"Message content: {update['message']['text']}\n" \
                  f"{traceback.format_exc()}\n" \
                  f"{context.error.__class__.__name__}: {context.error}"
        self.admin_broadcast(message)
        logger.error(message)

    def admin_broadcast(self, message):
        for chat_id in get_group_members('Admins'):
            self.bot.send_message(chat_id, message)
