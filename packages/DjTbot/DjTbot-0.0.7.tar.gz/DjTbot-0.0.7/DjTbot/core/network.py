# -*- coding: utf-8 -*-
import logging
import ssl
import os
from six.moves.urllib.request import urlopen
from six.moves.urllib.error import URLError


logger = logging.getLogger('tbot')
context = ssl._create_unverified_context()


def wait_for_internet(http_proxy=None):
    if http_proxy:
        os.environ['http_proxy'] = http_proxy
        os.environ['https_proxy'] = http_proxy

    while True:
        try:
            urlopen('https://www.google.com', timeout=1, context=context)
            return
        except URLError:
            logging.info('Waiting for internet connection')
