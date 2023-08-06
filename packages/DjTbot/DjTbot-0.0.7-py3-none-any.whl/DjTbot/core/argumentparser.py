import argparse
from abc import ABCMeta, abstractmethod


class TelegramArgumentParser(argparse.ArgumentParser, metaclass=ABCMeta):
    error_message = None

    def __init__(self, *args, **kwargs):
        super(TelegramArgumentParser, self).__init__(*args, **kwargs)
        self.add_arguments()

    def _print_message(self, message, file=None):
        pass

    def exit(self, status=0, message=None):
        if message:
            self.error_message = message

    @abstractmethod
    def add_arguments(self):
        pass

    @staticmethod
    @abstractmethod
    def factory(command_class_name):
        pass
