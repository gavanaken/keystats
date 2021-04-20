# -------------------------
# keystats
# Filename: mainloop.py
# Copyright: (c) 2021
# Author: GregVanAken
# ------------------------
from messaging.format import KeyEvent
from messaging.consumer import Consumer
import json
import os
import pandas as pd
import time

OUTPUT = 'data.csv'


def main():
    if not os.path.exists(OUTPUT):
        df = pd.DataFrame(columns=[k for k in KeyEvent.__annotations__.keys()])
    else:
        df = pd.read_csv(OUTPUT)

    consumer = Consumer()
    while True:
        data = consumer.read()
        if data:
            event = KeyEvent(json=data)
            newline = list(json.loads(event.json()).values())
            df = df.append(pd.Series(newline, index=df.columns), ignore_index=True)
            df.to_csv(OUTPUT, index=False)
            print(f'{len(df)}| {event}')
        else:
            time.sleep(0.1)


if __name__ == '__main__':
    main()
