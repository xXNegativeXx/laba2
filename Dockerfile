FROM python

WORKDIR /app

ADD . /app/

RUN pip install --trusted-host pypl.python.org flask

CMD [ "python", "main.py"]
