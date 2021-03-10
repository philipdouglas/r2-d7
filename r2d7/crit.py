import copy
from html import unescape
from itertools import chain, groupby
import logging
import re
import random

from r2d7.core import DroidCore, UserError
from r2d7.cardlookup import CardLookup

logger = logging.getLogger(__name__)


class CritRandom(CardLookup):
    def __init__(self):


    def load_data(self):
        super().load_data()



