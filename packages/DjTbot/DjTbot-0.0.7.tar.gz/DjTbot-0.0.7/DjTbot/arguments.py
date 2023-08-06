from abc import ABCMeta, abstractmethod
from DjTbot.core.argumentparser import TelegramArgumentParser


class TBotArgumentParser(TelegramArgumentParser, metaclass=ABCMeta):
    @abstractmethod
    def add_arguments(self):
        pass

    @staticmethod
    def factory(command_class_name):
        parsers = {
            'AddGroupCommand': TelegramIDGroupArgumentParser,
        }
        return parsers[command_class_name]()


class TelegramIDGroupArgumentParser(TBotArgumentParser):
    def add_arguments(self):
        self.add_argument('telegram_id', type=int)
        self.add_argument('group')
