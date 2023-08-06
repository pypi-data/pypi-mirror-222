import logging
import random
from abc import ABCMeta, abstractmethod
from .errors import TelegramBotError, MethodNotDefinedError
from .giphy import giphy
from DjTbot.utils import get_group_members, get_user_groups, get_all_ids

logger = logging.getLogger("tbot")

HELP = {}


class AuthorizedCommand(object, metaclass=ABCMeta):
    denied_giphy_set = None  # 'dragon-ball'
    allowed_groups = []

    def __call__(self, update, context):
        chat_id = self.get_chat_id(update)
        if self.authorized(chat_id):
            self.run(update, context)
        else:
            self.block(context.bot, chat_id)

    @staticmethod
    def get_chat_id(update):
        return update.message.chat_id

    def block(self, bot, chat_id):
        bot.sendDocument(document=self.denied_giphy(), chat_id=chat_id)
        unauthorized_message = 'Unauthorized access: chat_id = {}'.format(chat_id)
        self.admin_broadcast(bot, unauthorized_message)
        logger.warning(unauthorized_message)

    def authorized(self, chat_id):
        if chat_id in self.restricted_to or '*' in self.allowed_groups:
            if chat_id in get_all_ids():
                return True
        return False

    def denied_giphy(self):
        if self.denied_giphy_set:
            return self.random_giphy(self.denied_giphy_set)
        else:
            return self.random_giphy()

    @staticmethod
    def random_giphy(giphy_set='denied'):
        img = random.choice(giphy[giphy_set])
        return img

    @staticmethod
    def admin_broadcast(bot, message):
        for chat_id in get_group_members('Admins'):
            bot.send_message(chat_id, message)

    @property
    def restricted_to(self):
        allowed_users = set(get_group_members('Admins'))
        for group in self.allowed_groups:
            [allowed_users.add(user) for user in get_group_members(group)]
        return allowed_users

    @abstractmethod
    def run(self, update, context):
        pass


class Command(AuthorizedCommand, metaclass=ABCMeta):
    command = None
    usage = '/{}'
    help_text = ''
    start_message = 'Espera que miro...'

    def __init__(self):
        super(Command, self).__init__()
        if self.command is None:
            raise TelegramBotError('{}: Must define command attribute'.format(self.__class__.__name__))

        if self.help_text == '':
            raise TelegramBotError('{}: Must define command attribute'.format(self.__class__.__name__))

    def send_ussage(self, bot, update):
        bot.sendMessage(chat_id=self.get_chat_id(update), text=self.usage)

    def send_running_message(self, bot, update):
        bot.sendMessage(chat_id=self.get_chat_id(update), text=self.start_message)

    @property
    def help(self):
        if isinstance(self.help_text, list):
            cmds = ['/' + cmd for cmd in self.command]
        else:
            cmds = [f'/{self.command}']
        return f"{', '.join(cmds)}: {self.help_text}"

    def get_user_groups(self, update):
        return get_user_groups(self.get_chat_id(update))

    @abstractmethod
    def run(self, update, context):
        pass


class CommandWithArgumentsMixin(object, metaclass=ABCMeta):
    argument_parser = None
    usage = None
    argument_parser_factory_class = None

    def run(self, update, context):
        self.check_argument_parser_factory_class()
        self.argument_parser = self.get_argument_parser()
        arguments = self.argument_parser.parse_args(context.args)
        if self.argument_parser.error_message:
            context.bot.sendMessage(chat_id=update.message.chat_id,
                                    text=f"Invalid Arguments:\n{self.argument_parser.error_message}\n{self.usage}\n")
        else:
            self.command_call(arguments, update, context)

    def check_argument_parser_factory_class(self):
        if self.argument_parser_factory_class is None:
            raise AttributeError(f"{self.__class__.__name__} argument_parser_factory_class is not set\n"
                                 f"Example: {self.__class__.__name__}.argument_parser_factory_class = ArgumentParser\n"
                                 f"ArgumentParser must be a subclass of \n"
                                 f"tbot.core.argumentparser.TelegramArgumentParser\n"
                                 f"Check example at: https://git.herrerosolis.com/cookiecutters/django-telegram-bot")

    def command_call(self, arguments, update, context):
        raise MethodNotDefinedError(f"{self.__class__.__name__}: "
                                    f"Subclasses using CommandWithArgumentsMixin must define command_call method")

    def get_argument_parser(self):
        return self.argument_parser_factory_class.factory(self.__class__.__name__)
