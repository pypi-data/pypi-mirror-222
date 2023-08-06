import os

from browser import html, document, timer
from .utils import LocalInterpreter
import inspect
from string import ascii_lowercase
import random
import logging
import json

RadiantServer = None


# # ----------------------------------------------------------------------
# def delay(t):
    # """"""
    # def wrap(fn):
        # def inset(*args, **kwargs):
            # print(f'DELAYING: {t}')
            # return timer.set_timeout(lambda: fn(*args, **kwargs), t)
        # return inset
    # return wrap


########################################################################
class RadiantAPI:
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, class_, python=[[None, None, None]], **kwargs):
        """"""

        print('#' * 10)
        print(python)
        for module, class_, endpoint in python:
            if module and module != 'None':
                setattr(self, class_, LocalInterpreter(endpoint=endpoint))

        self.body = document.select_one('body')
        self.head = document.select_one('head')

    # ----------------------------------------------------------------------
    def add_css_file(self, file):
        """"""
        document.select('head')[0] <= html.LINK(
            href=os.path.join('root', file), type='text/css', rel='stylesheet')

    # # ----------------------------------------------------------------------
    # def on_load(self, callback, evt='DOMContentLoaded'):
        # """"""
        # logging.warning('#' * 30)
        # logging.warning('#' * 30)
        # document.addEventListener('load', callback)
        # logging.warning('#' * 30)
        # logging.warning('#' * 30)

