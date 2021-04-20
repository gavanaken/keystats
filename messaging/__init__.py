# -------------------------
# keystats
# Filename: __init__.py
# Copyright: (c) 2021
# Author: GregVanAken
# ------------------------
import os
from enum import Enum
BROKER_SERVERS = os.getenv('BROKER_SERVERS', 'localhost:9092')  # comma-separated


class TOPICS(str, Enum):
    """Message topics"""
    KeyData = 'KEY-DATA'
