# -------------------------
# keystats
# Filename: mainloop.py
# Copyright: (c) 2021
# Author: GregVanAken
# ------------------------
from messaging.format import KeyEvent
from messaging.consumer import Consumer
import json
import pandas as pd
import time
df = pd.DataFrame(columns=[k for k in KeyEvent.__annotations__.keys()])

consumer = Consumer()
while True:
    data = consumer.read()
    if data:
        event = KeyEvent(json=data)
        newline = list(json.loads(event.json()).values())
        print(newline)
        df.append(pd.Series(newline, index=df.columns), ignore_index=True)
        print(df)
    else:
        time.sleep(0.1)
