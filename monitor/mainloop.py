# -------------------------
# keystats
# Filename: mainloop.py
# Copyright: (c) 2021
# Author: GregVanAken
# ------------------------
import time

import keyboard
from messaging.format import KeyEvent, KeyType
from messaging.producer import Producer
from datetime import datetime


def main():
    """Initialize a producer and write key event messages."""
    producer = Producer()

    def on_release(key: keyboard.KeyboardEvent):
        key_type = KeyType.alphanum if len(key.name) == 1 and key.name.isascii() else KeyType.special
        event = KeyEvent(key_type, str(key.name), datetime.utcnow())
        producer.produce(event.json())
        print(event)

    keyboard.on_release(on_release)

    while True:
        time.sleep(0.01)


if __name__ == '__main__':
    main()
