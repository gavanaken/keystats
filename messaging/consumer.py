# -------------------------
# keystats
# Filename: consumer.py
# Copyright: (c) 2021
# Author: GregVanAken
# ------------------------
import confluent_kafka
from messaging import BROKER_SERVERS, TOPICS
import uuid
import os
from typing import Union


class Consumer:
    """Abstraction of a consumer that reads messages"""
    _consumer: confluent_kafka.Consumer = None
    _brokers: str = None

    def __init__(self, topics: list = None, brokers: str = BROKER_SERVERS):
        if topics is None:
            topics = [t.value for t in TOPICS]
        self._topics = topics
        self._brokers = brokers
        _lcl = os.path.normpath(__file__)
        self._id = f'{".".join(_lcl.split(os.sep)[-3:])}.{str(uuid.uuid4())}'
        self._consumer = confluent_kafka.Consumer({
            'bootstrap.servers': self._brokers,
            'group.id': self._id,
            'auto.offset.reset': 'latest'
        })
        self._consumer.subscribe(self._topics)

    def read(self) -> Union[str, None]:
        """Check for a message and return it"""
        msg: confluent_kafka.Message = self._consumer.poll(0.1)
        if msg is None:
            return None
        if msg.error():
            return None
        return msg.value()

    def __str__(self) -> str:
        """Get a description of this consumer for logging"""
        return f'Consumer: #{self._id}\n' \
               f'\tConnected: [{self._brokers}]\n' \
               f'\tListening: {self._topics}'
