# -------------------------
# keystats
# Filename: producer.py
# Copyright: (c) 2021
# Author: GregVanAken
# ------------------------
import confluent_kafka
from messaging import BROKER_SERVERS, TOPICS
from typing import Union


class Producer:
    """Abstraction of a producer that can send messages"""
    _producer: confluent_kafka.Producer = None
    _brokers: str = None

    def __init__(self, brokers: str = BROKER_SERVERS):
        self._brokers = brokers
        self._producer = confluent_kafka.Producer({'bootstrap.servers': self._brokers})

    def produce(self, data: Union[str, bytes], topic=TOPICS.KeyData):
        """Send the data as a message"""
        self._producer.poll(0)
        self._producer.produce(topic, data)
