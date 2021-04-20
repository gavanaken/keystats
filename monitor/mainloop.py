# -------------------------
# keystats
# Filename: mainloop.py
# Copyright: (c) 2021
# Author: GregVanAken
# ------------------------
from pynput import keyboard
from messaging.format import KeyEvent, KeyType
from messaging.producer import Producer
from datetime import datetime


def main():
    """Initialize a producer and write key event messages."""
    producer = Producer()

    def on_release(key):
        key_type = KeyType.alphanum if 'char' in dir(key) else KeyType.special
        event = KeyEvent(key_type, str(key), datetime.utcnow())
        producer.produce(event.json())
        print(event)

    with keyboard.Listener(
            on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    main()
