FROM python:3.9.4-buster

WORKDIR /usr/src/app

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONPATH="/user/src/app:${PYTHONPATH}"

CMD ["python", "archive/mainloop.py"]
