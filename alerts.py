import json
import ssl
from pprint import pprint
from colorama import init, Fore, Style
from kafka import KafkaConsumer


class TetrationAlertHandler():
    """
    Class responsible for refreshing collecting alerts from the Kafka stream
    coming from Tetration Analytics
    """

    def __init__(self):
        # Load Kafka topic configuration for tenant
        self.ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        self.ssl_context.options |= ssl.OP_NO_SSLv2
        self.ssl_context.options |= ssl.OP_NO_SSLv3
        self.ssl_context.options |= ssl.OP_NO_TLSv1
        self.ssl_context.options |= ssl.OP_NO_TLSv1_1
        self.update_count = 1
        topic = open('credentials/topic.txt', 'r').read()
        brokers = open('credentials/kafkaBrokerIps.txt', 'r').read().split(',')

        print('Loading certificates...')
        # Connect to the Kafka topic
        self.ssl_context.load_cert_chain('credentials/kafkaConsumerCA.cert',
                                         'credentials/kafkaConsumerPrivateKey.key')
        print('Starting Kafka client...')
        self.kafka_client = KafkaConsumer(bootstrap_servers=brokers,
                                          security_protocol='SSL',
                                          ssl_context=self.ssl_context)
        print('Subscribing to', topic)
        self.kafka_client.subscribe(topic)

    def get_alerts(self):
        print('Waiting for alerts...')
        for message in self.kafka_client:
            details = json.loads(message.value)
            print(Fore.GREEN + Style.BRIGHT + details["alert_text_with_names"] + Fore.RESET + Style.DIM)
            pprint(details["alert_details_json"])
            print(Style.RESET_ALL)


if __name__ == '__main__':
    init()
    msg_handler = TetrationAlertHandler()
    msg_handler.get_alerts()
