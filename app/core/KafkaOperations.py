from kafka import KafkaAdminClient
from kafka import KafkaProducer
from kafka import KafkaConsumer
from app import Config


def get_consumer_groups():
    consumer = KafkaAdminClient(bootstrap_servers=Config.Links.KAFKA_HOSTS)
    for group in consumer.list_consumer_groups():
        print(group[0])


def send_message_in_room(room_name):
    bootstrap_servers = Config.Links.KAFKA_HOSTS

    room_name = room_name

    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    message_data = input("Enter message: ")
    producer.send(room_name, str.encode(message_data))
    print("Message Sent!")


def read_messages_in_room(room_name):
    consumer = KafkaConsumer(bootstrap_servers=Config.Links.KAFKA_HOSTS, auto_offset_reset='earliest')
    consumer.subscribe(room_name)

    for msg in consumer:
        print("Message from Producer on Topic - " + msg.topic + ":" + msg.value.decode())
