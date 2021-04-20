# -------------------------
# keystats
# Filename: format.py
# Copyright: (c) 2021
# Author: GregVanAken
# ------------------------

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import json


class KeyType(str, Enum):
    """Types of keys"""
    alphanum = 'alphanum'
    special = 'special'


@dataclass
class KeyEvent:
    """A single key press event"""
    type: KeyType
    key: str
    utc: datetime

    def json(self) -> str:
        return json.dumps({k: str(v).strip("'") for k, v in self.__dict__.items()})

    def __init__(self, *args, **kwargs):
        if args:
            self.type, self.key, self.utc = args
        if kwargs.get('json', None):
            fields = json.loads(kwargs['json'])
            self.type = KeyType(fields.get('type', None).split('.')[1])
            self.key = fields.get('key', None)
            self.utc = datetime.strptime(fields.get('utc', None), '%Y-%m-%d %H:%M:%S.%f')

    def __str__(self):
        return self.__class__.__name__ + ': { ' + ', '.join([f'.{k}={v}' for k, v in self.__dict__.items()]) + ' }'
