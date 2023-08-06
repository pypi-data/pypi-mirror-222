"""Package dealing with managing taxtrees.

A taxcodeset is defined as a set of taxcodes. It is represented as (a json string of) a list of
taxcodes.
"""

from .base import Taxtree, load_taxtree
from .extra import *


__all__ = ["Taxtree", "load_taxtree", "LeafsetMapper"]
