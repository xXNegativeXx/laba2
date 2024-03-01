import time
import uvicorn
import pika
from fastapi import FastAPI
import logging

logging.basicConfig(level='INFO', format="%(levelname)s - %(asctime)s - %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    logger.info('Соединение с брокером сообщений установлено')
    channel.queue_declare(queue='hello')

    number = 0
    while number < 10:
        time.sleep(5)
        channel.basic_publish(exchange='', routing_key='hello', body=f'Hi World! {number}')
        # print(f" [{number}] Sent message")
        logger.info(f'Сообщение {number} отправлено в очередь')
        number += 1
    connection.close()
except:
    logger.critical('Соединение с брокером не установлено')

# app = FastAPI(title='Service1')


# @app.get('/service1')
# def get_service1():
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
#     channel = connection.channel()
#     channel.queue_declare(queue='hello')
#
#     number = 0
#     while number < 50:
#         time.sleep(5)
#         channel.basic_publish(exchange='', routing_key='hello', body='Hi World!')
#         print(f" {number} Sent message")
#         number += 1
#     connection.close()
#     return {"Service 1"}
#
#
# if __name__ == '__main__':
#     uvicorn.run("main:app", host='0.0.0.0', port=7040, reload=True)

