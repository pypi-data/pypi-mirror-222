from hci_framework.radiant.utils import environ
from confluent_kafka import Producer
import logging


########################################################################
class KafkaLogging(logging.Handler):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """"""
        super().__init__()

        self.topic = environ('SERVICE_NAME', 'logs')
        formatter = logging.Formatter(f'{self.topic}:%(asctime)s: %(levelname)s - %(message)s')
        self.setFormatter(formatter)
        self.producer = Producer({'bootstrap.servers': 'kafka-logs-service:9093'})

    # ----------------------------------------------------------------------
    def emit(self, record):
        """"""
        log_message = self.format(record)
        self.producer.produce(self.topic, value=log_message)
        self.producer.flush()


custom_handler = KafkaLogging()
custom_handler.setLevel(logging.INFO)

root_logger = logging.getLogger()
root_logger.addHandler(custom_handler)
