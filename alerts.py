import json
import ssl
import time
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
        self.ssl_context.load_cert_chain('credentials/kafkaConsumerCA.cert', 'credentials/kafkaConsumerPrivateKey.key')
        print('Starting Kafka client...')
        self.kafka_client = KafkaConsumer(bootstrap_servers=brokers,
                                          security_protocol='SSL',
                                          ssl_context=self.ssl_context)
        print('Subscribing to', topic)
        self.kafka_client.subscribe(topic)

    def print_alert_time(self, details):
        try:
            alert_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(details["alert_time"] / 1000))
        except KeyError:
            alert_time = "No time given"
        print(Fore.WHITE + Style.BRIGHT + alert_time)

    def print_alert_header(self, details):
        text = details.get("alert_text_with_names", details.get("alert_text", "No provided alert text"))
        print(Fore.GREEN + Style.BRIGHT + text + Fore.RESET + Style.DIM)

    def print_alert_detail(self, details):
        try:
            pprint(details["alert_details_json"], compact=True, width=160)
        except KeyError:
            try:
                alert_details = json.loads(details["alert_details"])
                pprint(alert_details, compact=True, width=160)
            except (KeyError, json.JSONDecodeError):
                print(Fore.RED + "Warning - could not find alert details. Dumping whole alert" + Fore.RESET)
                pprint(details)
        print(Style.RESET_ALL)

    def print_alert(self, details):
        self.print_alert_time(details)
        self.print_alert_header(details)
        self.print_alert_detail(details)

    def get_alerts(self):
        print('Waiting for alerts...')
        for message in self.kafka_client:
            details = json.loads(message.value)
            self.print_alert(details)


if __name__ == '__main__':
    init()
    msg_handler = TetrationAlertHandler()
    msg_handler.get_alerts()
