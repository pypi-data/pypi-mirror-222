import logging
from .commands import AuthorizedCommand


logger = logging.getLogger("tbot")


class Listener(AuthorizedCommand):
    denied_giphy_set = 'denied'
    filters = None

    def run(self, update, context):
        raise NotImplementedError('{} Must implement __call__ method'.format(self.__class__.__name__))

